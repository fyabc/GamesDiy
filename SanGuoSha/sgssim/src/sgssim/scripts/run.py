#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse

from sgssim.core.extension import load_all_extensions
from sgssim.core.engines import create_engine_from_config
from sgssim.support.logging_utils import setup_logging
from sgssim.ui.cli import SgsCliApp


def main():
    parser = argparse.ArgumentParser(description='Simple SanGuoSha Runner')

    # Global arguments.
    parser.add_argument('-u', '--ui', choices=['cli'], default='cli',
                        help='UI mode, default to %(default)r')
    parser.add_argument('-c', '--config', type=str, default='builtin:rp:1-2-4-1', help='Game config')
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
