import pytest

from sgssim.core.hero import Hero, Gender


class TestGender:
    def test_male(self):
        assert Gender.MALE.is_male
        assert not Gender.MALE.is_female

    def test_female(self):
        assert Gender.FEMALE.is_female
        assert not Gender.FEMALE.is_male

    def test_both(self):
        assert Gender.BOTH.is_male
        assert Gender.BOTH.is_female

    def test_same_gender(self):
        assert Gender.MALE.same_gender(Gender.MALE)
        assert Gender.BOTH.same_gender(Gender.MALE)
        assert Gender.MALE.same_gender(Gender.BOTH)
        assert not Gender.MALE.same_gender(Gender.FEMALE)

    def test_opposite_gender(self):
        assert Gender.MALE.opposite_gender(Gender.FEMALE)
        assert Gender.BOTH.opposite_gender(Gender.MALE)


class TestHero:
    def test_create_hero(self):
        hero = Hero(
            id='test-hero',
            name='Test Hero',
            faction='Wei',
            sub_faction='',
            gender=Gender.MALE,
            init_hp=4,
            init_max_hp=4,
            init_armor=0,
        )
        assert hero.id == 'test-hero'
        assert hero.name == 'Test Hero'
        assert hero.faction == 'Wei'
        assert hero.init_hp == 4
        assert hero.skills == []
        assert hero.perfect_matches == []

    def test_dummy_heroes_exist(self):
        from sgssim.core.hero import DUMMY_HEROES
        assert len(DUMMY_HEROES) == 2
        assert DUMMY_HEROES[0].id == '士兵-男'
        assert DUMMY_HEROES[1].id == '士兵-女'
