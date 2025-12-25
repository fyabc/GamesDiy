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
