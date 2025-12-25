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


class ActiveSkill(Skill):
    """主动技：可以在出牌阶段空闲时间点使用的技能。

    例：官方标貂蝉【离间】。
    """


class TriggerSkill(Skill):
    """触发技：在某条件下可被触发的技能。

    例：官方标黄月英【集智】。
    """


class AuraSkill(Skill):
    """光环技：在某条件下固定生效的技能。

    例：官方标陆逊【谦逊】。
    """
