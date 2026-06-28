#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import dataclasses
from enum import IntEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .skill import Skill


# Types.
HeroIDType = str
HeroDB = dict[HeroIDType, 'Hero']


class Gender(IntEnum):
    INVALID = 0
    MALE = 1
    FEMALE = 2
    NONE = 3
    BOTH = 4

    @property
    def is_male(self) -> bool:
        return self == Gender.MALE or self == Gender.BOTH

    @property
    def is_female(self) -> bool:
        return self == Gender.FEMALE or self == Gender.BOTH

    def same_gender(self, other: 'Gender') -> bool:
        return self == Gender.BOTH or other == Gender.BOTH or self == other

    def opposite_gender(self, other: 'Gender') -> bool:
        return self == Gender.BOTH or other == Gender.BOTH or self != other


@dataclasses.dataclass
class Hero:
    """武将类。

    注：此类不包括武将技能，仅包括基础信息。
    """

    id: HeroIDType      # 武将ID，区分不同版本的同名武将
    name: str           # 姓名
    faction: str        # 主势力
    sub_faction: str    # 次势力
    gender: Gender
    init_hp: int
    init_max_hp: int
    init_armor: int

    skills: list['Skill'] = dataclasses.field(default_factory=list)

    perfect_matches: list[str] = dataclasses.field(default_factory=list)    # 珠联璧合


DUMMY_HEROES = [
    Hero(
        id="士兵-男",
        name="士兵-男",
        faction="群",
        sub_faction="群",
        gender=Gender.MALE,
        init_hp=4,
        init_max_hp=4,
        init_armor=0,
        skills=[],
        perfect_matches=["士兵-女"],
    ),
    Hero(
        id="士兵-女",
        name="士兵-女",
        faction="群",
        sub_faction="群",
        gender=Gender.FEMALE,
        init_hp=4,
        init_max_hp=4,
        init_armor=0,
        skills=[],
        perfect_matches=[],
    ),
]
