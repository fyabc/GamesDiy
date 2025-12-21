#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import dataclasses
from enum import Enum, IntEnum
from typing import Optional


class Suit(IntEnum):
    """花色枚举类"""
    NO_SUIT = 0     # 无色牌
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4


class Value(IntEnum):
    """点数枚举类"""
    NO_VALUE = 0
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


@dataclasses.dataclass
class CardTypeValue:
    """牌类别值类"""
    t1: str                     # 主类别
    t2: Optional[str] = None    # 子类别
    t3: Optional[str] = None    # 细分子类别

    @property
    def type(self, i: int = 0):
        if i == 0:
            return self.t1
        elif i == 1:
            return self.t2
        elif i == 2:
            return self.t3
        else:
            raise ValueError("Invalid index")


class CardType(CardTypeValue, Enum):
    """牌类别枚举类"""
    NO_TYPE = CardTypeValue("无类别", None, None)

    # B = Basic
    B_DEFAULT = ("基本牌", None, None)

    B_SLASH_DEFAULT = ("基本牌", "杀", None)
    B_SLASH_COMMON = ("基本牌", "杀", "普通杀")
    B_SLASH_THUNDER = ("基本牌", "杀", "雷杀")
    B_SLASH_FIRE = ("基本牌", "杀", "火杀")
    B_SLASH_ICE = ("基本牌", "杀", "冰杀")
    B_SLASH_SHOT = ("基本牌", "杀", "射杀")
    B_SLASH_ASS = ("基本牌", "杀", "暗杀")
    B_SLASH_BLOOD = ("基本牌", "杀", "血杀")

    B_DODGE = ("基本牌", "闪", None)
    B_PEACH = ("基本牌", "桃", None)
    B_SPIRITS = ("基本牌", "酒", None)
    B_POISON = ("基本牌", "毒", None)

    # S = Strategy
    S_DEFAULT = ("锦囊牌", None, None)
    S_COMMON = ("锦囊牌", "普通锦囊牌", None)
    S_DELAYED = ("锦囊牌", "延时锦囊牌", None)

    # E = Equipment
    E_DEFAULT = ("装备牌", None, None)
    E_WEAPON = ("装备牌", "武器牌", None)
    E_ARMOR = ("装备牌", "防具牌", None)
    E_HORSE_ATK = ("装备牌", "进攻马牌", None)
    E_HORSE_DEF = ("装备牌", "防御马牌", None)
    E_TREASURE = ("装备牌", "宝物牌", None)

    # === Basic type checks === #

    @property
    def is_basic(self):
        return self.value.t1 == "基本牌"

    @property
    def is_strategy(self):
        return self.value in [
            CardType.S_DEFAULT,
            CardType.S_COMMON,
            CardType.S_DELAYED,
        ]

    @property
    def is_equipment(self):
        return self.value in [
            CardType.E_DEFAULT,
            CardType.E_WEAPON,
            CardType.E_ARMOR,
            CardType.E_HORSE_ATK,
            CardType.E_HORSE_DEF,
            CardType.E_TREASURE,
        ]

    # === Sub type checks === #

    @property
    def is_slash(self):
        return self.value.t1 == "基本牌" and self.value.t2 == "杀"

    # === Other type checks === #

    @property
    def is_immediate(self):
        """即时牌（【杀】或普通锦囊牌）"""
        return self.is_basic or self.value == CardType.S_COMMON


@dataclasses.dataclass
class Card:
    suit: Suit
    value: Value
    type: CardType
