#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import logging

from .extension import ALL_EXTENSIONS


class BaseEngine:
    def __init__(self):
        pass

    def setup(self):
        logging.info('Initializing engine ...')

        for extension in sorted(ALL_EXTENSIONS.values(), key=lambda ext: (ext.priority, ext.id)):
            logging.info(f'Including extension {extension.id!r} into engine ...')
            pass

    def run(self):
        pass
