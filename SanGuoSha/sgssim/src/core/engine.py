#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import List

from .deck import Deck
from .player import Player


class BaseEngine:
    def __init__(self):
        pass

    def run(self):
        pass


class RolePlayEngine(BaseEngine):
    """身份模式"""

    def __init__(self):
        super().__init__()

        self.players: List[Player] = []
        self.deck: Deck = Deck()
