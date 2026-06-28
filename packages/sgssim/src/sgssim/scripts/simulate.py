#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
from typing import Annotated, Optional

import typer

from sgssim.core.extension import load_all_extensions
from sgssim.core.engines import create_engine_from_config
from sgssim.support.logging_utils import setup_logging

app = typer.Typer(add_completion=False)


@app.command(help="""\
Simulate SanGuoSha games.

[1mConfig syntax (-c / --config):[0m

  builtin:rp:<players>    Built-in roleplay mode, <players> can be:
    2 / 1-0-1-0             2-player  (1 主公 vs 1 反贼)
    5 / 1-1-2-1             5-player  (1 主公 + 1 忠臣 + 2 反贼 + 1 内奸)
    8 / 1-2-4-1             8-player  (1 主公 + 2 忠臣 + 4 反贼 + 1 内奸)
  <json-file>             Load config from a JSON file.
                          JSON must have a "mode" field ("rp" / "roleplay")
                          and a "roles" field mapping role names to counts.

[1mExamples:[0m

  sgs-sim -c builtin:rp:2 -n 100       Run 100 two-player simulations
  sgs-sim -c builtin:rp:8 -s 42        8-player with fixed seed 42
  sgs-sim -c my_config.json -l debug   Load JSON config with debug logging
""")
def simulate(
    config: Annotated[
        str,
        typer.Option('-c', '--config', help='Game config (see above for syntax).'),
    ] = 'builtin:rp:1-2-4-1',
    seed: Annotated[
        Optional[int],
        typer.Option('-s', '--seed', help='Base random seed, simulation#N will use seed + N.'),
    ] = None,
    n_sim: Annotated[
        int,
        typer.Option('-n', '--n-sim', help='Number of simulations to run.'),
    ] = 1,
    log_level: Annotated[
        str,
        typer.Option('-l', '--log-level', help='Logging level.'),
    ] = 'warning',
):
    setup_logging(log_level=log_level)

    load_all_extensions()

    engine = create_engine_from_config(config_str=config, seed=seed)
    engine.setup(run_config={})

    for i in range(n_sim):
        logging.debug(f'Simulation #{i} ...')

        engine.reset_states()
        engine.run()

        if engine.seed is not None:
            engine.seed += 1


def main():
    app()


if __name__ == '__main__':
    main()
