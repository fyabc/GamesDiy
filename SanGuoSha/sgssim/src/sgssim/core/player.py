#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import dataclasses

from .hero import Hero
from .card import Card


@dataclasses.dataclass
class Player:
    index: int  # 座位（0为一号位）

    heroes: list[Hero]      # 武将牌

    hp: int
    max_hp: int
    armor: int

    hand: list[Card]        # 体力值
    judge_area: list[Card]  # 手牌区

    # 装备区
    weapon: Card = None
    guard: Card = None
    horse_atk: Card = None
    horse_def: Card = None
    treasure: Card = None

    flipped: bool = False   # 是否被翻面
    chained: bool = False   # 是否被横置
