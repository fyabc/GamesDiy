#! /usr/bin/env python
# -*- encoding: utf-8 -*-

# Types.
SkillIDType = str
SkillDB = dict[SkillIDType, 'Skill']


class Skill:
    """技能类。"""

    id: SkillIDType     # 技能ID，区分不同版本的同名技能
    name: str           # 技能名称
    tags: list[str]     # 技能标签（主公技、锁定技等）


class ViewAsSkill(Skill):
    """视为技

    例：官方标关羽【武圣】。
    """


class ActiveSkill(Skill):
    """主动技

    例：官方标貂蝉【离间】。
    """


class AuraSkill(Skill):
    """光环技

    例：官方标陆逊【谦逊】。
    """
