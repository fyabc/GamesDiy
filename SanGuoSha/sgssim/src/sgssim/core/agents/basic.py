#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Some basic agents."""

from .agent import Agent
from ..player import Player
from ..hero import Hero


class RandomAgent(Agent):
    """随机选择"""

    @property
    def rng(self):
        return self.engine.rng

    def choose_heroes(self, candidates: list[list['Hero']]) -> list['Hero']:
        return self.rng.choice(candidates)

    def choose_player(self, candidates: list[Player]) -> Player:
        return self.rng.choice(candidates)

    def active_action(self):
        return None
