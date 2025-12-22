#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import logging


def setup_logging():
    from rich.logging import RichHandler
    handlers = [RichHandler()]

    logging.basicConfig(
        format='%(message)s',
        datefmt='%m/%d %H:%M:%S',
        level=logging.INFO,
        handlers=handlers,
    )

    from rich.traceback import install
    install()
