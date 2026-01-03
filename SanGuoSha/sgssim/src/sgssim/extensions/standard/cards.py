#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Standard cards."""

from sgssim.core.card import CardProto, CardType
from sgssim.core.agents import Agent


class Strike(CardProto):
    id = "普通杀"
    name = "杀"
    type = CardType.B_STRIKE_DEFAULT

    def play(self, agent: Agent):
        pass


class Dodge(CardProto):
    id = "闪"
    name = "闪"
    type = CardType.B_DODGE

    def play(self, agent: Agent):
        pass


class Peach(CardProto):
    id = "桃"
    name = "桃"
    type = CardType.B_PEACH

    def play(self, agent: Agent):
        pass


class Spirits(CardProto):
    id = "酒"
    name = "酒"
    type = CardType.B_SPIRITS

    def play(self, agent: Agent):
        pass
