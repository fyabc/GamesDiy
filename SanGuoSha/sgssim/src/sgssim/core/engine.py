#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import logging

from .extension import ALL_EXTENSIONS


class BaseEngine:
    def __init__(self):
        pass

    def setup(self):
        logging.info('Initializing engine ...')

        for ext_id, extension in ALL_EXTENSIONS.items():
            logging.info(f'Including extension {ext_id!r} into engine ...')
            pass

    def run(self):
        pass
