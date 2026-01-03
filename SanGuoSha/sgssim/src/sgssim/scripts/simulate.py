#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse
import logging

from sgssim.core.extension import load_all_extensions
from sgssim.core.engines import create_engine_from_config
from sgssim.support.logging_utils import setup_logging


def main():
    parser = argparse.ArgumentParser(description='Simulate SanGuoSha')
    parser.add_argument('-c', '--config', type=str, default='builtin:rp:1-2-4-1', help='Game config')
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
