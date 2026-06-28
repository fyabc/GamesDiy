from unittest.mock import patch, MagicMock

from typer.testing import CliRunner

from sgssim.scripts.run import app


runner = CliRunner()


class TestRunHelp:
    def test_help_exit_code(self):
        result = runner.invoke(app, ['--help'])
        assert result.exit_code == 0

    def test_help_shows_description(self):
        result = runner.invoke(app, ['--help'])
        assert 'SanGuoSha Runner' in result.output

    def test_help_shows_all_options(self):
        result = runner.invoke(app, ['--help'])
        for flag in ['--ui', '-u', '--config', '-c', '--seed', '-s', '--log-level', '-l']:
            assert flag in result.output, f'{flag} missing from help'

    def test_help_shows_config_syntax(self):
        result = runner.invoke(app, ['--help'])
        assert 'builtin:rp:' in result.output

    def test_help_shows_default_config(self):
        result = runner.invoke(app, ['--help'])
        assert 'builtin:rp:1-2-4-1' in result.output


class TestRunExecution:
    def test_default_options(self):
        mock_engine = MagicMock()
        with patch('sgssim.scripts.run.load_all_extensions'), \
             patch('sgssim.scripts.run.create_engine_from_config', return_value=mock_engine), \
             patch('sgssim.scripts.run.SgsCliApp') as mock_cli_app:
            result = runner.invoke(app)

        assert result.exit_code == 0
        mock_engine.setup.assert_called_once_with(run_config={})
        mock_cli_app.assert_called_once_with(mock_engine)
        mock_cli_app.return_value.run.assert_called_once()

    def test_config_passed_to_engine(self):
        mock_engine = MagicMock()
        with patch('sgssim.scripts.run.load_all_extensions'), \
             patch('sgssim.scripts.run.create_engine_from_config', return_value=mock_engine) as mock_create, \
             patch('sgssim.scripts.run.SgsCliApp'):
            result = runner.invoke(app, ['-c', 'builtin:rp:2'])

        assert result.exit_code == 0
        mock_create.assert_called_once_with(config_str='builtin:rp:2', seed=None)

    def test_seed_passed_to_engine(self):
        mock_engine = MagicMock()
        with patch('sgssim.scripts.run.load_all_extensions'), \
             patch('sgssim.scripts.run.create_engine_from_config', return_value=mock_engine) as mock_create, \
             patch('sgssim.scripts.run.SgsCliApp'):
            result = runner.invoke(app, ['-s', '42'])

        assert result.exit_code == 0
        mock_create.assert_called_once_with(config_str='builtin:rp:1-2-4-1', seed=42)

    def test_all_options_combined(self):
        mock_engine = MagicMock()
        with patch('sgssim.scripts.run.load_all_extensions'), \
             patch('sgssim.scripts.run.create_engine_from_config', return_value=mock_engine) as mock_create, \
             patch('sgssim.scripts.run.SgsCliApp'):
            result = runner.invoke(app, [
                '-u', 'cli',
                '-c', 'builtin:rp:5',
                '-s', '99',
                '-l', 'info',
            ])

        assert result.exit_code == 0
        mock_create.assert_called_once_with(config_str='builtin:rp:5', seed=99)

    def test_invalid_config_produces_error(self):
        with patch('sgssim.scripts.run.load_all_extensions'), \
             patch('sgssim.scripts.run.create_engine_from_config',
                   side_effect=ValueError('Unknown mode: bad')):
            result = runner.invoke(app, ['-c', 'bad_config.json'])

        assert result.exit_code != 0
        assert isinstance(result.exception, ValueError)
        assert 'Unknown' in str(result.exception)
