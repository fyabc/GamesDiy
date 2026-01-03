#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import dataclasses
from enum import Enum, IntEnum
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .agents.agent import Agent

# Types.
CardIDType = str
CardProtoDB = dict[CardIDType, 'CardProto']


class Suit(Enum):
    """花色枚举类"""
    NO_SUIT = "无花色"
    SPADE = "♠"
    HEART = "♥"
    CLUB = "♣"
    DIAMOND = "♦"


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

    B_STRIKE_DEFAULT = ("基本牌", "杀", None)
    B_STRIKE_COMMON = ("基本牌", "杀", "普通杀")
    B_STRIKE_THUNDER = ("基本牌", "杀", "雷杀")
    B_STRIKE_FIRE = ("基本牌", "杀", "火杀")
    B_STRIKE_ICE = ("基本牌", "杀", "冰杀")
    B_STRIKE_SHOT = ("基本牌", "杀", "射杀")
    B_STRIKE_ASS = ("基本牌", "杀", "暗杀")
    B_STRIKE_BLOOD = ("基本牌", "杀", "血杀")

    B_DODGE = ("基本牌", "闪", None)
    B_PEACH = ("基本牌", "桃", None)
    B_SPIRITS = ("基本牌", "酒", None)
    B_POISON = ("基本牌", "毒", None)
    B_SHADOW = ("基本牌", "影", None)

    # S = Scroll
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
    def is_scroll(self):
        return self.value.t1 == "锦囊牌"

    @property
    def is_equipment(self):
        return self.value.t1 == "装备牌"

    # === Sub type checks === #

    @property
    def is_strike(self):
        return self.value.t1 == "基本牌" and self.value.t2 == "杀"

    # === Other type checks === #


class Area(Enum):
    INVALID = "无效区域"

    DECK = "牌堆"
    DISCARDED = "弃牌堆"
    HAND = "手牌区"
    HAND_VISIBLE = "明置手牌区"
    EQUIPMENT = "装备区"
    JUDGE = "判定区"
    PROCESSING = "处理区"
    EXCLUDED = "除外区"
    REN = "仁区"


class CardProto:
    """Card prototype, include general card attributed (id, name, type, play, etc.).

    Extensions should extend this class to add their new cards.
    """

    id: CardIDType
    name: str
    type: CardType

    def play(self, agent: 'Agent'):
        """Play this card."""


@dataclasses.dataclass
class Card:
    """Card instance, include card-specific attributes (suit, value, area, etc.)."""

    proto: CardProto

    extension: str  # 所属扩展

    suit: Suit
    value: Value
    area: Area = Area.INVALID

    @classmethod
    def from_json(cls, card_protos: CardProtoDB, card_dict: dict, extension: str) -> 'Card':
        card_id = card_dict.get('id', None)
        if card_id is None:
            raise ValueError(f'Card dict {card_dict} does not contains `id` field.')
        assert isinstance(card_id, str)
        card_proto = card_protos.get(card_id, None)
        if card_proto is None:
            raise ValueError(f'Card proto {card_id!r} does not exists.')

        suit = Suit(card_dict.get('suit', None))
        value = Value(card_dict.get('value', None))

        return cls(
            proto=card_proto,
            extension=extension,
            suit=suit,
            value=value,
        )
