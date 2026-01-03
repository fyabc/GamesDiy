#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Event


class GameStart(Event):
    """游戏开始"""


class RoundStart(Event):
    """轮开始"""

    def __init__(self, round_num: int):
        self.round_num = round_num

    def __rich__(self):
        return f"[yellow]RoundStart({self.round_num})[/]"


class RoundEnd(Event):
    """轮结束"""

    def __init__(self, round_num: int):
        self.round_num = round_num

    def __rich__(self):
        return f"[yellow]RoundEnd({self.round_num})[/]"


class TurnStart(Event):
    """回合开始"""

    def __init__(self, turn_num: int):
        self.turn_num = turn_num

    def __rich__(self):
        return f"[yellow]TurnStart({self.turn_num})[/]"


class TurnEnd(Event):
    """回合结束"""

    def __init__(self, turn_num: int):
        self.turn_num = turn_num

    def __rich__(self):
        return f"[yellow]TurnEnd({self.turn_num})[/]"
