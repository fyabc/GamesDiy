import pytest

from sgssim.core.engines.roleplay import Roles, BUILTIN_RP_CONFIGS


class TestRoles:
    def test_all_roles_exist(self):
        assert Roles.MONARCH.value == '主公'
        assert Roles.MINISTER.value == '忠臣'
        assert Roles.REBEL.value == '反贼'
        assert Roles.TURN_COAT.value == '内奸'
        assert Roles.NONE.value == '无身份'

    def test_colored_values(self):
        assert '[red]' in Roles.MONARCH.colored_value
        assert '[yellow]' in Roles.MINISTER.colored_value
        assert '[green]' in Roles.REBEL.colored_value
        assert '[blue]' in Roles.TURN_COAT.colored_value

    def test_none_role_has_no_color(self):
        assert '[' not in Roles.NONE.colored_value


class TestBuiltinRpConfigs:
    def test_2p_config(self):
        config = BUILTIN_RP_CONFIGS['1-0-1-0']
        assert config['roles'] == {'主公': 1, '反贼': 1}
        assert sum(config['roles'].values()) == 2

    def test_5p_config(self):
        config = BUILTIN_RP_CONFIGS['1-1-2-1']
        assert config['roles'] == {'主公': 1, '忠臣': 1, '反贼': 2, '内奸': 1}
        assert sum(config['roles'].values()) == 5

    def test_8p_config(self):
        config = BUILTIN_RP_CONFIGS['1-2-4-1']
        assert config['roles'] == {'主公': 1, '忠臣': 2, '反贼': 4, '内奸': 1}
        assert sum(config['roles'].values()) == 8

    def test_aliases(self):
        assert BUILTIN_RP_CONFIGS['2'] is BUILTIN_RP_CONFIGS['1-0-1-0']
        assert BUILTIN_RP_CONFIGS['8'] is BUILTIN_RP_CONFIGS['1-2-4-1']
