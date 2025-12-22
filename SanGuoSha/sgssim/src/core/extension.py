#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Extension class."""

from typing import Dict


class Extension:
    def __init__(self, ext_id: str):
        self.id = ext_id


_ALL_EXTENSIONS: Dict[str, Extension] = {}
