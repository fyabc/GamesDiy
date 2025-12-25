#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from ..player import Player


class Agent:
    """Agent base class.

    Interact with cards and skills, provide play actions to them.

    All interation methods are **async**, since they may represent time-cost user operations.

    :param player: Player bound to this agent.
    """

    def __init__(self, player: Player):
        self.player = player

    async def choose_player(self, candidates: list[Player]) -> Player:
        """Choose a player from candidates."""
        raise NotImplementedError()
