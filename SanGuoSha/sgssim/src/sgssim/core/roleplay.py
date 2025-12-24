#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from enum import Enum

from .deck import Deck
from .engine import BaseEngine
from .player import Player


class Roles(Enum):
    MONARCH = "主公"
    MINISTER = "忠臣"
    REBEL = "反贼"
    TURN_COAT = "内奸"


class RolePlayEngine(BaseEngine):
    """身份模式"""

    def __init__(self):
        super().__init__()

        self.players: list[Player] = []
        self.deck: Deck = Deck()
