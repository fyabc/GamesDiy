#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from collections import deque

from .card import Card


class Deck:
    MAX_SIZE = 300

    def __init__(self):
        self.cards: deque[Card] = deque(maxlen=self.MAX_SIZE)   # 牌堆
        self.discarded: list[Card] = []     # 弃牌堆
