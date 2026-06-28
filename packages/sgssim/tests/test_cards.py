import pytest

from sgssim.core.card import Card, CardProto, CardType, Suit, Value, Area


class TestCardProto:
    def test_create_card_proto(self):
        proto = CardProto()
        proto.id = 'test-strike'
        proto.name = '杀'
        proto.type = CardType.B_STRIKE_COMMON
        assert proto.id == 'test-strike'
        assert proto.name == '杀'
        assert proto.type.is_basic
        assert proto.type.is_strike


class TestCard:
    @pytest.fixture
    def proto_db(self):
        proto = CardProto()
        proto.id = 'test-card'
        proto.name = 'Test Card'
        proto.type = CardType.B_PEACH
        return {'test-card': proto}

    def test_from_json_valid(self, proto_db):
        card_dict = {'id': 'test-card', 'suit': '♠', 'value': 7}
        card = Card.from_json(proto_db, card_dict, extension='test')
        assert card.proto is proto_db['test-card']
        assert card.suit == Suit.SPADE
        assert card.value == Value.SEVEN
        assert card.extension == 'test'
        assert card.area == Area.INVALID

    def test_from_json_missing_id(self, proto_db):
        card_dict = {'suit': '♥', 'value': 1}
        with pytest.raises(ValueError, match='id'):
            Card.from_json(proto_db, card_dict, extension='test')

    def test_from_json_unknown_proto(self, proto_db):
        card_dict = {'id': 'nonexistent', 'suit': '♦', 'value': 1}
        with pytest.raises(ValueError, match='nonexistent'):
            Card.from_json(proto_db, card_dict, extension='test')


class TestCardType:
    def test_basic_card_checks(self):
        assert CardType.B_STRIKE_DEFAULT.is_basic
        assert CardType.B_PEACH.is_basic
        assert not CardType.B_STRIKE_DEFAULT.is_scroll
        assert not CardType.B_STRIKE_DEFAULT.is_equipment

    def test_scroll_card_checks(self):
        assert CardType.S_DEFAULT.is_scroll
        assert not CardType.S_DEFAULT.is_basic

    def test_equipment_card_checks(self):
        assert CardType.E_WEAPON.is_equipment
        assert not CardType.E_WEAPON.is_basic

    def test_strike_subtype(self):
        assert CardType.B_STRIKE_THUNDER.is_strike
        assert CardType.B_STRIKE_FIRE.is_strike
        assert not CardType.B_PEACH.is_strike
