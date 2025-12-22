#! /usr/bin/env python
# -*- encoding: utf-8 -*-


class Player:
    def __init__(self):
        # 武将牌
        self.heroes = []

        # 体力值
        self.hp: int = 5

        # 手牌区
        self.hand = []

        # 判定区
        self.judge_area = []

        # 装备区
        self.weapon = None
        self.guard = None
        self.horse_atk = None
        self.horse_def = None
        self.treasure = None
