#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import logging


def setup_logging(log_level: str = 'WARNING'):
    from rich.logging import RichHandler
    handlers = [RichHandler()]

    logging.basicConfig(
        format='%(message)s',
        datefmt='%m/%d %H:%M:%S',
        level=log_level.upper(),
        handlers=handlers,
    )

    from rich.traceback import install
    install()
