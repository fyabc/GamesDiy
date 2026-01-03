#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import TYPE_CHECKING

from ..player import Player

if TYPE_CHECKING:
    from ..engines import BaseEngine
    from ..hero import Hero


class Agent:
    """Agent base class.

    Interact with cards and skills, provide play actions to them.

    :param player: Player bound to this agent.
    """

    def __init__(self, engine: 'BaseEngine', player: Player):
        self.engine = engine
        self.player = player

    def choose_heroes(self, candidates: list[list['Hero']]) -> list['Hero']:
        """选将"""
        raise NotImplementedError()

    def choose_player(self, candidates: list[Player]) -> Player:
        """选择目标角色"""
        raise NotImplementedError()

    def active_action(self):
        """出牌阶段空闲时间点操作

        此方法会被反复调用直到返回None，表示结束出牌"""
        raise NotImplementedError()
