#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse
import logging

from sgssim.core.extension import load_all_extensions
from sgssim.core.engines import create_engine_from_config
from sgssim.support.logging_utils import setup_logging


def main():
    parser = argparse.ArgumentParser(
        description='Simulate SanGuoSha',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Config syntax (-c / --config):
  builtin:rp:<players>    Built-in roleplay mode, <players> can be:
    2 / 1-0-1-0             2-player  (1 主公 vs 1 反贼)
    5 / 1-1-2-1             5-player  (1 主公 + 1 忠臣 + 2 反贼 + 1 内奸)
    8 / 1-2-4-1             8-player  (1 主公 + 2 忠臣 + 4 反贼 + 1 内奸)
  <json-file>             Load config from a JSON file.
                          JSON must have a "mode" field ("rp" / "roleplay")
                          and a "roles" field mapping role names to counts.

Examples:
  sgs-sim -c builtin:rp:2 -n 100       Run 100 two-player simulations
  sgs-sim -c builtin:rp:8 -s 42        8-player with fixed seed 42
  sgs-sim -c my_config.json -l debug   Load JSON config with debug logging
""")
    parser.add_argument('-c', '--config', type=str, default='builtin:rp:1-2-4-1',
                        help='Game config (see below for syntax)')
    parser.add_argument('-s', '--seed', type=int, default=None, help='Base random seed, simulation#N will use `seed + N`.')
    parser.add_argument('-n', '--n-sim', type=int, default=1, help='#runs to simulate, default to %(default)r')
    parser.add_argument('-l', '--log-level', choices=['debug', 'info', 'warning', 'error', 'critical'], default='warning',
                        help='Logging level, default to %(default)r')

    args = parser.parse_args()

    setup_logging(log_level=args.log_level)

    load_all_extensions()

    engine = create_engine_from_config(config_str=args.config, seed=args.seed)
    engine.setup(run_config={})

    for i in range(args.n_sim):
        logging.debug(f'Simulation #{i} ...')

        engine.reset_states()
        engine.run()

        if engine.seed is not None:
            engine.seed += 1


if __name__ == '__main__':
    main()
