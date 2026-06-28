from unittest.mock import patch, MagicMock

from typer.testing import CliRunner

from sgssim.scripts.simulate import app


runner = CliRunner()


class TestSimulateHelp:
    def test_help_exit_code(self):
        result = runner.invoke(app, ['--help'])
        assert result.exit_code == 0

    def test_help_shows_description(self):
        result = runner.invoke(app, ['--help'])
        assert 'Simulate SanGuoSha' in result.output

    def test_help_shows_all_options(self):
        result = runner.invoke(app, ['--help'])
        for flag in ['--config', '-c', '--seed', '-s', '--n-sim', '-n', '--log-level', '-l']:
            assert flag in result.output, f'{flag} missing from help'

    def test_help_shows_config_syntax(self):
        result = runner.invoke(app, ['--help'])
        assert 'builtin:rp:' in result.output
        assert 'json-file' in result.output.lower() or '<json-file>' in result.output

    def test_help_shows_defaults(self):
        result = runner.invoke(app, ['--help'])
        assert 'builtin:rp:1-2-4-1' in result.output


class TestSimulateExecution:
    def _make_mock_engine(self, seed=None):
        engine = MagicMock()
        engine.seed = seed
        return engine

    def test_default_options(self):
        mock_engine = self._make_mock_engine()
        with patch('sgssim.scripts.simulate.load_all_extensions'), \
             patch('sgssim.scripts.simulate.create_engine_from_config', return_value=mock_engine):
            result = runner.invoke(app)

        assert result.exit_code == 0
        mock_engine.setup.assert_called_once_with(run_config={})
        mock_engine.run.assert_called_once()

    def test_n_sim_controls_run_count(self):
        mock_engine = self._make_mock_engine()
        with patch('sgssim.scripts.simulate.load_all_extensions'), \
             patch('sgssim.scripts.simulate.create_engine_from_config', return_value=mock_engine):
            result = runner.invoke(app, ['-n', '5'])

        assert result.exit_code == 0
        assert mock_engine.run.call_count == 5
        assert mock_engine.reset_states.call_count == 5

    def test_config_passed_to_engine(self):
        mock_engine = self._make_mock_engine()
        with patch('sgssim.scripts.simulate.load_all_extensions'), \
             patch('sgssim.scripts.simulate.create_engine_from_config', return_value=mock_engine) as mock_create:
            result = runner.invoke(app, ['-c', 'builtin:rp:2'])

        assert result.exit_code == 0
        mock_create.assert_called_once_with(config_str='builtin:rp:2', seed=None)

    def test_seed_passed_to_engine(self):
        mock_engine = self._make_mock_engine()
        with patch('sgssim.scripts.simulate.load_all_extensions'), \
             patch('sgssim.scripts.simulate.create_engine_from_config', return_value=mock_engine) as mock_create:
            result = runner.invoke(app, ['-s', '42'])

        assert result.exit_code == 0
        mock_create.assert_called_once_with(config_str='builtin:rp:1-2-4-1', seed=42)

    def test_seed_increments_each_run(self):
        mock_engine = self._make_mock_engine(seed=100)
        with patch('sgssim.scripts.simulate.load_all_extensions'), \
             patch('sgssim.scripts.simulate.create_engine_from_config', return_value=mock_engine):
            result = runner.invoke(app, ['-n', '3'])

        assert result.exit_code == 0
        assert mock_engine.seed == 103  # 100 + 3 increments

    def test_seed_not_incremented_when_none(self):
        mock_engine = self._make_mock_engine(seed=None)
        with patch('sgssim.scripts.simulate.load_all_extensions'), \
             patch('sgssim.scripts.simulate.create_engine_from_config', return_value=mock_engine):
            result = runner.invoke(app, ['-n', '3'])

        assert result.exit_code == 0
        assert mock_engine.seed is None

    def test_invalid_config_produces_error(self):
        with patch('sgssim.scripts.simulate.load_all_extensions'), \
             patch('sgssim.scripts.simulate.create_engine_from_config',
                   side_effect=ValueError('Unknown builtin roleplay config: unknown')):
            result = runner.invoke(app, ['-c', 'builtin:rp:unknown'])

        assert result.exit_code != 0
        assert isinstance(result.exception, ValueError)
        assert 'Unknown' in str(result.exception)

    def test_all_options_combined(self):
        mock_engine = self._make_mock_engine(seed=10)
        with patch('sgssim.scripts.simulate.load_all_extensions'), \
             patch('sgssim.scripts.simulate.create_engine_from_config', return_value=mock_engine) as mock_create:
            result = runner.invoke(app, [
                '-c', 'builtin:rp:5',
                '-s', '10',
                '-n', '2',
                '-l', 'debug',
            ])

        assert result.exit_code == 0
        mock_create.assert_called_once_with(config_str='builtin:rp:5', seed=10)
        assert mock_engine.run.call_count == 2
        assert mock_engine.seed == 12  # 10 + 2
