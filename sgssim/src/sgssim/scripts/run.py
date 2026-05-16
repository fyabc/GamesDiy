#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse

from sgssim.core.extension import load_all_extensions
from sgssim.core.engines import create_engine_from_config
from sgssim.support.logging_utils import setup_logging
from sgssim.ui.cli import SgsCliApp


def main():
    parser = argparse.ArgumentParser(
        description='Simple SanGuoSha Runner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Config syntax (-c / --config):
  builtin:rp:<players>    Built-in roleplay mode, <players> can be:
    2 / 1-0-1-0             2-player  (1 主公 vs 1 反贼)
    5 / 1-1-2-1             5-player  (1 主公 + 1 忠臣 + 2 反贼 + 1 内奸)
    8 / 1-2-4-1             8-player  (1 主公 + 2 忠臣 + 4 反贼 + 1 内奸)
  <json-file>             Load config from a JSON file.

Examples:
  sgs-run -c builtin:rp:2          Launch interactive 2-player game
  sgs-run -c my_config.json -s 42  Load JSON config with fixed seed
""")

    # Global arguments.
    parser.add_argument('-u', '--ui', choices=['cli'], default='cli',
                        help='UI mode, default to %(default)r')
    parser.add_argument('-c', '--config', type=str, default='builtin:rp:1-2-4-1',
                        help='Game config (see below for syntax)')
    parser.add_argument('-s', '--seed', type=int, default=None, help='Base random seed.')
    parser.add_argument('-l', '--log-level', choices=['debug', 'info', 'warning', 'error', 'critical'], default='warning',
                        help='Logging level, default to %(default)r')

    args = parser.parse_args()

    setup_logging(log_level=args.log_level)

    load_all_extensions()

    engine = create_engine_from_config(config_str=args.config, seed=args.seed)
    engine.setup(run_config={})

    app = SgsCliApp(engine)
    app.run()


if __name__ == '__main__':
    main()
