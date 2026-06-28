import pytest

from sgssim.core.extension import load_all_extensions
from sgssim.core.engines import create_engine_from_config


@pytest.fixture(scope='session', autouse=True)
def load_extensions():
    """Load all extensions once per test session."""
    load_all_extensions()


@pytest.fixture
def engine_2p():
    """2-player engine (1 主公 vs 1 反贼)."""
    engine = create_engine_from_config('builtin:rp:2')
    engine.setup(run_config={})
    return engine


@pytest.fixture
def engine_5p():
    """5-player engine (1 主公 + 1 忠臣 + 2 反贼 + 1 内奸)."""
    engine = create_engine_from_config('builtin:rp:5')
    engine.setup(run_config={})
    return engine


@pytest.fixture
def engine_8p():
    """8-player engine (1 主公 + 2 忠臣 + 4 反贼 + 1 内奸)."""
    engine = create_engine_from_config('builtin:rp:8')
    engine.setup(run_config={})
    return engine
