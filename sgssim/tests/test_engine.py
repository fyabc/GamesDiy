import pytest

from sgssim.core.engines import create_engine_from_config
from sgssim.core.engines.roleplay import RolePlayEngine, BUILTIN_RP_CONFIGS, Roles
from sgssim.core.engines.phases import Phase


class TestEngineCreation:
    def test_builtin_rp_2p(self):
        engine = create_engine_from_config('builtin:rp:2')
        assert isinstance(engine, RolePlayEngine)
        assert engine.num_players == 2

    def test_builtin_rp_5p(self):
        engine = create_engine_from_config('builtin:rp:5')
        assert isinstance(engine, RolePlayEngine)
        assert engine.num_players == 5

    def test_builtin_rp_8p(self):
        engine = create_engine_from_config('builtin:rp:8')
        assert isinstance(engine, RolePlayEngine)
        assert engine.num_players == 8

    def test_builtin_rp_full_config(self):
        engine = create_engine_from_config('builtin:rp:1-0-1-0')
        assert isinstance(engine, RolePlayEngine)
        assert engine.num_players == 2

    def test_unknown_builtin_config(self):
        with pytest.raises(ValueError, match='Unknown'):
            create_engine_from_config('builtin:rp:99')

    def test_unknown_builtin_mode(self):
        with pytest.raises(ValueError, match='Unknown'):
            create_engine_from_config('builtin:arena:8')


class TestEngineSetup:
    def test_setup_populates_players(self, engine_2p):
        assert len(engine_2p.players) == 2
        assert len(engine_2p.agents) == 2

    def test_setup_assigns_heroes(self, engine_2p):
        for player in engine_2p.players:
            assert len(player.heroes) == 1

    def test_setup_assigns_roles(self, engine_2p):
        roles = [p.extras['role'] for p in engine_2p.players]
        assert Roles.MONARCH in roles
        assert Roles.REBEL in roles

    def test_monarch_hp_bonus(self, engine_5p):
        """Monarch gets +1 HP only when total players >= 5."""
        for player in engine_5p.players:
            if player.extras['role'] == Roles.MONARCH:
                hero = player.heroes[0]
                assert player.max_hp == hero.init_max_hp + 1
                assert player.hp == hero.init_hp + 1

    def test_monarch_no_hp_bonus_in_2p(self, engine_2p):
        """2-player monarch should NOT get +1 HP bonus."""
        for player in engine_2p.players:
            hero = player.heroes[0]
            assert player.max_hp == hero.init_max_hp
            assert player.hp == hero.init_hp

    def test_non_monarch_no_hp_bonus(self, engine_5p):
        for player in engine_5p.players:
            if player.extras['role'] != Roles.MONARCH:
                hero = player.heroes[0]
                assert player.max_hp == hero.init_max_hp
                assert player.hp == hero.init_hp

    def test_setup_8p_roles(self, engine_8p):
        roles = [p.extras['role'] for p in engine_8p.players]
        assert roles.count(Roles.MONARCH) == 1
        assert roles.count(Roles.MINISTER) == 2
        assert roles.count(Roles.REBEL) == 4
        assert roles.count(Roles.TURN_COAT) == 1


class TestEngineRun:
    def test_reset_states(self, engine_2p):
        engine_2p.reset_states()
        assert engine_2p.current_round == 0
        assert engine_2p.current_turn == 0
        assert engine_2p.current_phase == Phase.OUT_OF_TURN

    def test_run_completes(self):
        """Engine should finish after reaching turn limit."""
        engine = create_engine_from_config('builtin:rp:2')
        engine.config = dict(engine.config, max_turns=5)
        engine.setup(run_config={})
        engine.run()
        assert engine.current_turn == 4

    def test_run_with_seed(self):
        engine = create_engine_from_config('builtin:rp:2', seed=42)
        engine.config = dict(engine.config, max_turns=5)
        engine.setup(run_config={})
        engine.run()
        assert engine.current_turn == 4


class TestJsonConfig:
    def test_load_json_config(self):
        import os
        assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
        config_path = os.path.join(assets_dir, 'sample_config_2p.json')
        engine = create_engine_from_config(config_path)
        assert isinstance(engine, RolePlayEngine)
        assert engine.num_players == 2

    def test_json_config_roles(self):
        import os
        assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
        config_path = os.path.join(assets_dir, 'sample_config_2p.json')
        engine = create_engine_from_config(config_path)
        engine.setup(run_config={})
        roles = [p.extras['role'] for p in engine.players]
        assert Roles.MONARCH in roles
        assert Roles.REBEL in roles

    def test_json_config_max_turns(self):
        import os
        assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
        config_path = os.path.join(assets_dir, 'sample_config_2p.json')
        engine = create_engine_from_config(config_path)
        engine.setup(run_config={})
        engine.run()
        assert engine.current_turn == 2  # max_turns=3 means 3 turns (0,1,2)


class TestMaxTurns:
    def test_default_max_turns(self):
        """Builtin configs without max_turns should default to 1_000_000."""
        engine = create_engine_from_config('builtin:rp:2')
        assert engine.config.get('max_turns', 1_000_000) == 1_000_000

    def test_custom_max_turns(self):
        engine = create_engine_from_config('builtin:rp:2')
        engine.config = dict(engine.config, max_turns=10)
        engine.setup(run_config={})
        engine.run()
        assert engine.current_turn == 9  # max_turns=10 means turns 0..9


class TestNextTurn:
    def test_next_turn_returns_false_when_game_continues(self):
        """next_turn should return False when game should continue."""
        engine = create_engine_from_config('builtin:rp:2')
        engine.config = dict(engine.config, max_turns=10)
        engine.setup(run_config={})
        result = engine.next_turn()
        assert result is False

    def test_next_turn_returns_true_when_game_ends(self):
        """next_turn should return True when game should end."""
        engine = create_engine_from_config('builtin:rp:2')
        engine.config = dict(engine.config, max_turns=1)
        engine.setup(run_config={})
        # current_turn=0, 0+1 >= 1 means game ends immediately.
        assert engine.next_turn() is True


class TestBuiltinConfigs:
    def test_2_is_alias(self):
        assert BUILTIN_RP_CONFIGS['2'] is BUILTIN_RP_CONFIGS['1-0-1-0']

    def test_8_is_alias(self):
        assert BUILTIN_RP_CONFIGS['8'] is BUILTIN_RP_CONFIGS['1-2-4-1']

    def test_all_configs_have_valid_structure(self):
        for name, config in BUILTIN_RP_CONFIGS.items():
            if name in ('2', '8'):
                continue  # Aliases, skip
            assert config['mode'] == 'roleplay'
            assert 'roles' in config
            assert sum(config['roles'].values()) >= 2
