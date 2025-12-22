#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse
import logging

from rich.console import Console

from src.core.card import CardType
from src.support.logging_utils import setup_logging

console = Console()


def _debug(args):
    for ct in CardType:
        logging.info(repr(ct))

    # app = SGSApp()
    # app.run()


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    setup_logging()

    _debug(args)


if __name__ == '__main__':
    main()
