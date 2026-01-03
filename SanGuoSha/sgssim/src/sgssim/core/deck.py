#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import random
from collections import deque
from typing import TYPE_CHECKING

from .card import Card, Area

if TYPE_CHECKING:
    from .engines import BaseEngine


class Deck:
    MAX_SIZE = 1024

    def __init__(self, engine: 'BaseEngine'):
        self.engine = engine
        self.cards: deque[Card] = deque(maxlen=self.MAX_SIZE)   # 牌堆
        self.discarded: list[Card] = []     # 弃牌堆

    def __rich__(self):
        return f"牌堆(剩余=[green]{len(self.cards)}[/]/弃牌堆=[red]{len(self.discarded)}[/])"

    def add_card(self, card: Card):
        self.cards.append(card)

    def shuffle(self):
        # Sort before shuffling.
        sorted_cards = sorted(self.cards, key=lambda c: id(c))
        self.cards.clear()
        self.cards.extend(sorted_cards)

        for card in self.cards:
            card.area = Area.DECK

        self.engine.rng.shuffle(self.cards)

    def reset(self):
        """Reset the deck. All cards in hand/processing/excluded/etc. should be discarded before call this method."""
        self.cards.extend(self.discarded)
        self.discarded.clear()
        self.shuffle()

        from .engines.events.card_events import DeckShuffled
        self.engine.push_event(DeckShuffled())

    def draw_cards(self, n: int = 1) -> list[Card]:
        out_cards = []
        for i in range(n):
            if not self.cards:
                self.reset()
            if not self.cards:
                from .engines.events.card_events import DeckExhausted
                self.engine.push_event(DeckExhausted())
                break
            card = self.cards.popleft()
            card.area = Area.HAND
            out_cards.append(card)
        return out_cards
