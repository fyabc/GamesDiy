import pytest
from pathlib import Path

from sgssim.core.extension import (
    Extension, ExtensionPriority, ALL_EXTENSIONS,
    add_extension, add_extension_from_path, load_all_extensions,
    BUILTIN_EXTENSION_ROOT,
)


@pytest.fixture(autouse=True)
def clean_extensions():
    """Reset extension state before each test."""
    ALL_EXTENSIONS.clear()
    yield
    ALL_EXTENSIONS.clear()


class TestExtension:
    def test_create_extension(self, tmp_path):
        ext = Extension('test-ext', tmp_path, priority=ExtensionPriority.DIY)
        assert ext.id == 'test-ext'
        assert ext.card_protos == {}
        assert ext.heroes == {}
        assert ext.skills == {}

    def test_create_extension_with_data(self, tmp_path):
        ext = Extension(
            'test-ext', tmp_path,
            card_protos={'a': 'proto_a'},
            heroes={'b': 'hero_b'},
            skills={'c': 'skill_c'},
        )
        assert ext.card_protos == {'a': 'proto_a'}
        assert ext.heroes == {'b': 'hero_b'}
        assert ext.skills == {'c': 'skill_c'}

    def test_load_card_list_json(self, tmp_path):
        card_list = tmp_path / 'card_list.json'
        card_list.write_text('[{"id": "test-card", "suit": "♠", "value": 7}]', encoding='utf-8')
        ext = Extension('test-ext', tmp_path)
        assert len(ext.card_list) == 1
        assert ext.card_list[0]['id'] == 'test-card'


class TestAddExtension:
    def test_add_extension(self, tmp_path):
        ext = Extension('test-ext', tmp_path)
        add_extension(ext)
        assert 'test-ext' in ALL_EXTENSIONS
        assert ALL_EXTENSIONS['test-ext'] is ext

    def test_add_duplicate_extension(self, tmp_path):
        ext = Extension('test-ext', tmp_path)
        add_extension(ext)
        with pytest.raises(ValueError, match='already exists'):
            add_extension(ext)

    def test_add_non_extension_instance(self):
        with pytest.raises(ValueError):
            add_extension('not-an-extension')

    def test_add_extension_without_id(self, tmp_path):
        ext = object()
        with pytest.raises(ValueError):
            add_extension(ext)


class TestLoadAllExtensions:
    def test_load_builtin_extensions(self):
        load_all_extensions()
        assert 'STANDARD' in ALL_EXTENSIONS


class TestBuiltinExtensionRoot:
    def test_root_exists(self):
        assert BUILTIN_EXTENSION_ROOT.exists()

    def test_standard_extension_present(self):
        standard_path = BUILTIN_EXTENSION_ROOT / 'standard'
        assert standard_path.exists()
        assert (standard_path / '__init__.py').exists()
