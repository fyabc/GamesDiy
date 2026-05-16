#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import TYPE_CHECKING

from .base import Event

if TYPE_CHECKING:
    from ...engines import BaseEngine
    from ...card import Card


class DispatchInitHand(Event):
    """分发起始手牌"""

    def __init__(self, player_idx: int, n: int):
        self.player_idx = player_idx
        self.n = n

    def __rich__(self):
        return f"[yellow]DispatchInitHand(P={self.player_idx}, n={self.n})[/]"

    def happen(self, engine: 'BaseEngine') -> 'list[Event]':
        player = engine.players[self.player_idx]
        cards = engine.deck.draw_cards(self.n)
        player.hand.extend(cards)
        return []


class DeckShuffled(Event):
    """牌堆洗牌"""


class DeckExhausted(Event):
    """牌堆耗尽"""


class DrawCards(Event):
    """摸牌"""

    def __init__(self, player_idx: int, n: int):
        self.player_idx = player_idx
        self.n = n

    def __rich__(self):
        return f"[yellow]DrawCards(P={self.player_idx}, n={self.n})[/]"

    def happen(self, engine: 'BaseEngine') -> 'list[Event]':
        player = engine.players[self.player_idx]
        cards = engine.deck.draw_cards(self.n)
        player.hand.extend(cards)
        return []


class DiscardCards(Event):
    """弃牌"""

    def __init__(self, player_idx: int, cards: 'list[Card]'):
        self.player_idx = player_idx
        self.cards = cards

    def __rich__(self):
        return f"[yellow]DiscardCards(P={self.player_idx}, cards=[{','.join(map(str, self.cards))}])[/]"

    def happen(self, engine: 'BaseEngine') -> 'list[Event]':
        player = engine.players[self.player_idx]

        # TODO

        return []
