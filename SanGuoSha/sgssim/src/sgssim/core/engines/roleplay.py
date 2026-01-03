#! /usr/bin/env python
# -*- encoding: utf-8 -*-
import logging
from enum import Enum
from typing import Optional, Any

from .engine import BaseEngine
from ..player import Player
from ..hero import DUMMY_HEROES


class Roles(Enum):
    NONE = "无身份"
    MONARCH = "主公"
    MINISTER = "忠臣"
    REBEL = "反贼"
    TURN_COAT = "内奸"

    @property
    def colored_value(self) -> str:
        if self == Roles.MONARCH:
            return f"[red]{self.value}[/]"
        elif self == Roles.MINISTER:
            return f"[yellow]{self.value}[/]"
        elif self == Roles.REBEL:
            return f"[green]{self.value}[/]"
        elif self == Roles.TURN_COAT:
            return f"[blue]{self.value}[/]"
        else:
            return self.value


BUILTIN_RP_CONFIGS = {
    '1-1-2-1': {
        'mode': 'roleplay',
        'roles': {'主公': 1, '忠臣': 1, '反贼': 2, '内奸': 1},
    },
    '1-2-4-1': {
        'mode': 'roleplay',
        'roles': {'主公': 1, '忠臣': 2, '反贼': 4, '内奸': 1},
    },
}
BUILTIN_RP_CONFIGS['8'] = BUILTIN_RP_CONFIGS['1-2-4-1']


class RolePlayEngine(BaseEngine):
    """身份模式"""

    def __init__(self, config: dict[str, Any], seed: Optional[int] = None):
        super().__init__(config, seed)

        self.num_players = sum(self.config['roles'].values())

    def setup(self, run_config: dict):
        super().setup(run_config=run_config)

        # Setup players & agents.

        # TODO: Setup from run_config.
        from ..agents.basic import RandomAgent

        roles = []
        for role, num in self.config['roles'].items():
            if role == "主公":
                continue
            for _ in range(num):
                roles.append(Roles(role))
        self.rng.shuffle(roles)
        roles.insert(0, Roles.MONARCH)

        for index in range(self.num_players):
            player = Player(index)
            player.extras['role'] = roles[index]
            self.players.append(player)
            self.agents.append(RandomAgent(self, player))

        # Select heroes.
        # TODO: Setup from heroes.
        for index in range(self.num_players):
            player = self.players[index]
            agent = self.agents[index]
            candidates = [[hero] for hero in DUMMY_HEROES]
            selected = agent.choose_heroes(candidates)[0]
            player.heroes = [selected]

        logging.info(f"Roleplay game setup finished.")

    def init_player_state(self, player):
        hero = player.heroes[0]
        if player.extras['role'] == Roles.MONARCH:
            player.hp = hero.init_hp + 1
            player.max_hp = hero.init_max_hp + 1
        else:
            player.hp = hero.init_hp
            player.max_hp = hero.init_max_hp
        player.armor = hero.init_armor

    def show_player_state(self, player: Player) -> str:
        return player.extras['role'].colored_value + ' ' + super().show_player_state(player)

    def check_game_end(self) -> bool:
        # TODO
        if self.current_turn >= 16:
            return True
        return False
