#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import dataclasses
from typing import Any, Generator, Optional

from .hero import Hero
from .card import Card


@dataclasses.dataclass
class Player:
    index: int  # 座位（0为一号位）

    alive: bool = True

    heroes: list[Hero] = dataclasses.field(default_factory=list)        # 武将牌

    hp: int = 1
    max_hp: int = 1
    armor: int = 0

    hand: list[Card] = dataclasses.field(default_factory=list)          # 手牌区
    judge_area: list[Card] = dataclasses.field(default_factory=list)    # 判定区

    # 装备区
    weapon: Optional[Card] = None
    guard: Optional[Card] = None
    horse_atk: Optional[Card] = None
    horse_def: Optional[Card] = None
    treasure: Optional[Card] = None

    flipped: bool = False   # 是否被翻面
    chained: bool = False   # 是否被横置

    # 其他数据
    extras: dict[str, Any] = dataclasses.field(default_factory=dict)

    def reset_hero_card(self):
        """复原武将牌"""
        self.flipped = False
        self.chained = False

    def reset_status(self, engine):
        """重置状态"""

        deck = engine.deck
        deck.discarded.extend(self.hand)
        self.hand.clear()
        deck.discarded.extend(self.judge_area)
        self.judge_area.clear()

        if self.weapon:
            deck.discarded.append(self.weapon)
            self.weapon = None
        if self.guard:
            deck.discarded.append(self.guard)
            self.guard = None
        if self.horse_atk:
            deck.discarded.append(self.horse_atk)
            self.horse_atk = None
        if self.horse_def:
            deck.discarded.append(self.horse_def)
            self.horse_def = None
        if self.treasure:
            deck.discarded.append(self.treasure)
            self.treasure = None

        self.reset_hero_card()

        engine.init_player_state(self)

        self.alive = True
