import pytest

from sgssim.core.player import Player
from sgssim.core.hero import Hero, Gender


@pytest.fixture
def dummy_engine():
    """Minimal mock engine with a deck for player reset."""
    class DummyDeck:
        def __init__(self):
            self.discarded = []

        def reset(self):
            pass

    class DummyEngine:
        def __init__(self):
            self.deck = DummyDeck()

        def init_player_state(self, player):
            player.hp = 4
            player.max_hp = 4

    return DummyEngine()


@pytest.fixture
def hero():
    return Hero(
        id='test', name='Test', faction='Wei', sub_faction='',
        gender=Gender.MALE, init_hp=4, init_max_hp=4, init_armor=0,
    )


class TestPlayer:
    def test_create_player(self):
        p = Player(index=0)
        assert p.index == 0
        assert p.alive is True
        assert p.heroes == []
        assert p.hand == []
        assert p.armor == 0

    def test_reset_status_clears_hand(self, dummy_engine, hero):
        p = Player(index=0)
        p.hand = ['card1', 'card2']
        p.reset_status(dummy_engine)
        assert p.hand == []
        assert len(dummy_engine.deck.discarded) == 2

    def test_reset_status_clears_judge_area(self, dummy_engine, hero):
        p = Player(index=0)
        p.judge_area = ['judge1']
        p.reset_status(dummy_engine)
        assert p.judge_area == []

    def test_reset_status_clears_equipment(self, dummy_engine, hero):
        p = Player(index=0)
        p.weapon = 'weapon'
        p.guard = 'guard'
        p.horse_atk = 'horse_atk'
        p.horse_def = 'horse_def'
        p.treasure = 'treasure'
        p.reset_status(dummy_engine)
        assert p.weapon is None
        assert p.guard is None
        assert p.horse_atk is None
        assert p.horse_def is None
        assert p.treasure is None

    def test_reset_hero_card(self, hero):
        p = Player(index=0)
        p.flipped = True
        p.chained = True
        p.reset_hero_card()
        assert p.flipped is False
        assert p.chained is False

    def test_reset_status_restores_alive(self, dummy_engine, hero):
        p = Player(index=0)
        p.alive = False
        p.reset_status(dummy_engine)
        assert p.alive is True
