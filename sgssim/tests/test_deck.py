import pytest

from sgssim.core.card import Card, CardProto, CardType, Suit, Value, Area
from sgssim.core.deck import Deck


class DummyEngine:
    def __init__(self):
        from random import Random
        self.rng = Random(42)

    def push_event(self, event):
        pass


class TestDeck:
    @pytest.fixture
    def engine(self):
        return DummyEngine()

    @pytest.fixture
    def deck(self, engine):
        return Deck(engine)

    @pytest.fixture
    def card_proto(self):
        proto = CardProto()
        proto.id = 'test-strike'
        proto.name = '杀'
        proto.type = CardType.B_STRIKE_COMMON
        return proto

    def test_add_card(self, deck, card_proto):
        card = Card(proto=card_proto, extension='test', suit=Suit.SPADE, value=Value.SEVEN)
        deck.add_card(card)
        assert len(deck.cards) == 1

    def test_draw_cards(self, deck, card_proto):
        for i in range(10):
            card = Card(proto=card_proto, extension='test', suit=Suit.SPADE, value=Value(i + 1))
            deck.add_card(card)
        drawn = deck.draw_cards(3)
        assert len(drawn) == 3
        assert all(c.area == Area.HAND for c in drawn)
        assert len(deck.cards) == 7

    def test_shuffle(self, deck, card_proto):
        for i in range(10):
            card = Card(proto=card_proto, extension='test', suit=Suit.SPADE, value=Value(i + 1))
            deck.add_card(card)
        deck.shuffle()
        assert len(deck.cards) == 10
        assert all(c.area == Area.DECK for c in deck.cards)

    def test_reset(self, deck, card_proto):
        for i in range(5):
            card = Card(proto=card_proto, extension='test', suit=Suit.SPADE, value=Value(i + 1))
            deck.add_card(card)
        deck.shuffle()
        drawn = deck.draw_cards(3)
        deck.discarded.extend(drawn)
        deck.reset()
        assert len(deck.cards) == 5
        assert len(deck.discarded) == 0

    def test_draw_empty_deck_resets(self, deck, card_proto):
        """When deck is empty, reset should refill from discard pile."""
        card = Card(proto=card_proto, extension='test', suit=Suit.SPADE, value=Value.ACE)
        deck.add_card(card)
        drawn = deck.draw_cards(1)
        deck.discarded.extend(drawn)
        # Now draw again - should trigger reset and redraw
        drawn2 = deck.draw_cards(1)
        assert len(drawn2) == 1
