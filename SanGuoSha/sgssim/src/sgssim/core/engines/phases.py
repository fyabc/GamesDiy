#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from enum import Enum


class Phase(Enum):
    """游戏阶段枚举"""

    OUT_OF_TURN = '非回合内'
    PREPARE = '准备阶段'
    JUDGE = '判定阶段'
    DRAW_CARD = '摸牌阶段'
    PLAY = '出牌阶段'
    DISCARD = '弃牌阶段'
    END = '结束阶段'
