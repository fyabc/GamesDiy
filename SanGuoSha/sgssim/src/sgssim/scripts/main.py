#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse

from sgssim.core.extension import load_all_extensions
from sgssim.core.roleplay import RolePlayEngine
from sgssim.support.logging_utils import setup_logging
from sgssim.ui.cli import SgsCliApp


def main():
    parser = argparse.ArgumentParser()

    # Global arguments.
    parser.add_argument('-u', '--ui', choices=['cli'], default='cli',
                        help='UI mode, default to %(default)r')
    parser.add_argument('-m', '--mode', choices=['roleplay'], default='roleplay',
                        help='Game mode, default to %(default)r')
    parser.add_argument('-l', '--log-level', choices=['debug', 'info', 'warning', 'error', 'critical'], default='warning',
                        help='Logging level, default to %(default)r')

    # Roleplay arguments.
    parser.add_argument('--role-counts', type=int, nargs=3, default=[2, 4, 1],
                        help='#players of each roles [忠臣数, 反贼数, 内奸数], default to %(default)r')

    args = parser.parse_args()

    setup_logging(log_level=args.log_level)

    load_all_extensions()

    engine = RolePlayEngine()
    engine.setup()

    app = SgsCliApp(engine)
    app.run()


if __name__ == '__main__':
    main()
