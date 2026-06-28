#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Annotated, Optional

import typer

from sgssim.core.extension import load_all_extensions
from sgssim.core.engines import create_engine_from_config
from sgssim.support.logging_utils import setup_logging
from sgssim.ui.cli import SgsCliApp

app = typer.Typer(add_completion=False)


@app.command(help="""\
Simple SanGuoSha Runner.

[1mConfig syntax (-c / --config):[0m

  builtin:rp:<players>    Built-in roleplay mode, <players> can be:
    2 / 1-0-1-0             2-player  (1 主公 vs 1 反贼)
    5 / 1-1-2-1             5-player  (1 主公 + 1 忠臣 + 2 反贼 + 1 内奸)
    8 / 1-2-4-1             8-player  (1 主公 + 2 忠臣 + 4 反贼 + 1 内奸)
  <json-file>             Load config from a JSON file.

[1mExamples:[0m

  sgs-run -c builtin:rp:2          Launch interactive 2-player game
  sgs-run -c my_config.json -s 42  Load JSON config with fixed seed
""")
def run(
    ui: Annotated[
        str,
        typer.Option('-u', '--ui', help='UI mode.'),
    ] = 'cli',
    config: Annotated[
        str,
        typer.Option('-c', '--config', help='Game config (see above for syntax).'),
    ] = 'builtin:rp:1-2-4-1',
    seed: Annotated[
        Optional[int],
        typer.Option('-s', '--seed', help='Base random seed.'),
    ] = None,
    log_level: Annotated[
        str,
        typer.Option('-l', '--log-level', help='Logging level.'),
    ] = 'warning',
):
    setup_logging(log_level=log_level)

    load_all_extensions()

    engine = create_engine_from_config(config_str=config, seed=seed)
    engine.setup(run_config={})

    cli_app = SgsCliApp(engine)
    cli_app.run()


def main():
    app()


if __name__ == '__main__':
    main()
