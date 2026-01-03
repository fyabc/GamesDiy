#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
from collections import deque, defaultdict
from random import Random
from typing import Optional, Any, TYPE_CHECKING

from rich.console import Console

from ..extension import ALL_EXTENSIONS
from ..card import Card, CardProtoDB
from ..hero import HeroDB
from ..player import Player
from ..skill import SkillDB
from ..deck import Deck
from .events import Event, Handler
from .phases import Phase

if TYPE_CHECKING:
    from ..agents.agent import Agent


console = Console()


class BaseEngine:
    def __init__(self, config: dict[str, Any], seed: Optional[int] = None):
        logging.info(f'Creating engine with config {config}')

        self.config = config
        self.seed = seed
        self.rng = Random(self.seed)
        self.echo = True

        # Game DBs: card protos, heroes, skills.
        self.card_protos: CardProtoDB = {}
        self.heroes: HeroDB = {}
        self.skills: SkillDB = {}

        # Game status: players, agents, deck.
        self.players: list[Player] = []
        self.agents: list['Agent'] = []
        self.deck = Deck(self)
        self.current_round: int = 0         # 当前轮数，0表示第一轮
        self.current_turn: int = 0          # 当前回合数，0表示第一回合
        self.current_player_idx: int = 0    # 当前玩家编号
        self._next_player_idx: int = 1      # 下一个玩家编号（不计额外回合）
        self._extra_turns: deque[int] = deque()     # 额外回合队列
        self.current_phase = Phase.OUT_OF_TURN

        # Event system.
        self.events: deque[Event] = deque()
        self.handlers: defaultdict[type[Event], list[Handler]] = defaultdict(list)

    def setup(self, run_config: dict):
        logging.info('Setting up engine ...')

        for extension in sorted(ALL_EXTENSIONS.values(), key=lambda ext: (ext.priority, ext.id)):
            logging.info(f'Including extension {extension.id!r} into engine ...')

            for cp_id, cp in extension.card_protos.items():
                if cp_id in self.card_protos:
                    raise ValueError(f'Card proto {cp_id!r} already exists.')
                self.card_protos[cp_id] = cp

            for hero_id, hero in extension.heroes.items():
                if hero_id in self.heroes:
                    raise ValueError(f'Hero {hero_id!r} already exists.')
                self.heroes[hero_id] = hero

            for skill_id, skill in extension.skills.items():
                if skill_id in self.skills:
                    raise ValueError(f'Skill {skill_id!r} already exists.')
                self.skills[skill_id] = skill

        for extension in sorted(ALL_EXTENSIONS.values(), key=lambda ext: (ext.priority, ext.id)):
            logging.info(f'Creating deck from extension {extension.id!r} into engine ...')
            for card_dict in extension.card_list:
                card = Card.from_json(self.card_protos, card_dict, extension=extension.id)
                self.deck.add_card(card)

    def reset_states(self):
        """Reset all game states.

        Subclasses should extend this method to clear their extra game states.
        """
        self.rng = Random(self.seed)

        # Reset all cards.
        for player in self.players:
            player.reset_status(self)
        self.deck.reset()

        self.current_round = 0
        self.current_turn = 0
        self.current_player_idx = 0
        self._next_player_idx = 1
        self._extra_turns.clear()
        self.current_phase = Phase.OUT_OF_TURN

        self.events.clear()
        self.handlers.clear()

    def init_player_state(self, player: Player):
        """Initialize player state. Different game mode can set their special rules."""

    def show_player_state(self, player: Player) -> str:
        if not player.heroes:
            hero_str = None
        elif len(player.heroes) == 1:
            hero_str = repr(player.heroes[0].name)
        else:
            hero_str = str([hero.name for hero in player.heroes])
        armor_str = ''
        if player.armor > 0:
            armor_str = f'[{player.armor}甲]'
        # TODO: Hands & Equips
        return f"玩家{player.index + 1} 武将={hero_str}, 体力={player.hp}/{player.max_hp}{armor_str}"

    @property
    def next_player_idx(self) -> int:
        if self._extra_turns:
            return self._extra_turns[0]
        else:
            return self._next_player_idx

    def next_turn(self):
        """Move to next turn."""
        from .events.global_events import RoundStart, RoundEnd, TurnStart, TurnEnd
        self.push_event(TurnEnd(self.current_turn))

        # Switch turn.
        if self._extra_turns:
            # 处理额外回合
            self.current_player_idx = self._extra_turns.popleft()
            self.current_turn += 1
            self.push_event(TurnStart(self.current_turn))
        else:
            if self._next_player_idx == 0:
                # 新一轮
                self.push_event(RoundEnd(self.current_round))
                self.current_player_idx = self._next_player_idx
                self._next_player_idx = 1
                self.current_round += 1
                self.current_turn += 1
                self.push_event(RoundStart(self.current_round))
                self.push_event(TurnStart(self.current_turn))
            else:
                self.current_player_idx = self._next_player_idx
                self._next_player_idx = (self._next_player_idx + 1) % len(self.players)
                self.current_turn += 1
                self.push_event(TurnStart(self.current_turn))

        if self.echo:
            console.print(f'[cyan]P> 第{self.current_round + 1}轮 第{self.current_turn + 1}回合 玩家{self.current_player_idx + 1}[/]')

    def insert_extra_turn(self, player_idx: int):
        self._extra_turns.append(player_idx)

    def check_game_end(self) -> bool:
        """Check if game is end."""
        raise NotImplementedError()

    def run(self):
        if self.echo:
            console.rule("[yellow]游戏开始", style='cyan')
            for player in self.players:
                console.print(self.show_player_state(player))
            console.print(self.deck)

        from .events.global_events import GameStart, RoundStart, TurnStart
        self.push_event(GameStart())

        # Dispatch initial hands.
        if self.echo:
            console.print('[cyan]P> 分配起始手牌[/]')

            from .events.card_events import DispatchInitHand
            for player_idx, player in enumerate(self.players):
                self.push_event(DispatchInitHand(player_idx, 4))

        if self.echo:
            console.print(f'[cyan]P> 第{self.current_round + 1}轮 第{self.current_turn + 1}回合 玩家{self.current_player_idx + 1}[/]')

        self.push_event(RoundStart(self.current_round))
        self.push_event(TurnStart(self.current_turn))

        # Game loop.
        while True:
            if self.check_game_end():
                break

            from .events.phase_events import (
                PreparePhaseStart,
                JudgePhaseStart,
                DrawCardPhaseStart,
                PlayPhaseStart,
                DiscardPhaseStart,
                EndPhaseStart,
                PreparePhaseEnd,
                JudgePhaseEnd,
                DrawCardPhaseEnd,
                PlayPhaseEnd,
                DiscardPhaseEnd,
                EndPhaseEnd,
            )

            self.push_event(PreparePhaseStart())
            self.push_event(PreparePhaseEnd())
            self.push_event(JudgePhaseStart())
            self.push_event(JudgePhaseEnd())
            self.push_event(DrawCardPhaseStart())
            self.push_event(DrawCardPhaseEnd())
            self.push_event(PlayPhaseStart())

            current_agent = self.agents[self.current_player_idx]
            while True:
                action = current_agent.active_action()
                if action is None:
                    break

            self.push_event(PlayPhaseEnd())
            self.push_event(DiscardPhaseStart())
            self.push_event(DiscardPhaseEnd())
            self.push_event(EndPhaseStart())
            self.push_event(EndPhaseEnd())

            self.next_turn()

        # Game end processing.

    def push_event(self, event: Event, handle: bool = True):
        self.events.append(event)
        if handle:
            self._handle_events()

    def _handle_events(self):
        while self.events:
            event = self.events.popleft()
            if self.echo:
                console.print('E> 处理事件：', event)
            consequences = event.happen(self)
            self.events.extend(consequences)
            # TODO
