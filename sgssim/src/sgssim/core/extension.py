#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""Extension class and utility functions."""

import json
import logging
import sys
import uuid
from enum import IntEnum
from importlib import util
from pathlib import Path
from typing import Dict, Any

from .card import CardProtoDB
from .hero import HeroDB
from .skill import SkillDB


CardListType = list[dict[str, Any]]


class ExtensionPriority(IntEnum):
    """Extensions with high priorities will be included before low priorities."""

    DEBUG = 100
    BUILTIN = 90
    DIY = 50


class Extension:
    def __init__(
        self,
        ext_id: str,
        ext_root_path: Path,
        priority: ExtensionPriority = ExtensionPriority.DIY,
        card_protos: CardProtoDB = None,
        heroes: HeroDB = None,
        skills: SkillDB = None,
    ):
        """Create extension.

        :param ext_id:
        :param ext_root_path:
        :param priority:
        :param card_protos: All new card prototypes in this extension.
        :param heroes: All new heroes in this extension.
        :param skills: All new skills in this extension.
        """
        self.id = ext_id
        self.priority = priority

        logging.info(f"Loading extension {self.id!r} from '{ext_root_path}' ...")

        self.card_protos = card_protos or {}
        self.heroes = heroes or {}
        self.skills = skills or {}

        self.card_list: CardListType = []
        card_list_path = ext_root_path / "card_list.json"
        if card_list_path.exists():
            with open(card_list_path, 'r', encoding='utf-8') as f:
                self.card_list = json.load(f)


BUILTIN_EXTENSION_ROOT = Path(__file__).absolute().parent.parent / 'extensions'
ALL_EXTENSIONS: Dict[str, Extension] = {}


def add_extension(ext: Extension):
    """Add an extension."""

    if not isinstance(ext, Extension):
        raise ValueError(f"Extension {ext} is not an instance of Extension.")

    ext_id = getattr(ext, 'id', None)
    if ext_id is None:
        raise ValueError(f"Extension {ext} does not have an id.")
    if ext.id in ALL_EXTENSIONS:
        raise ValueError(f"Extension {ext.id!r} already exists.")

    ALL_EXTENSIONS[ext.id] = ext


def add_extension_from_path(path: Path):
    """Load an extension from a path."""

    init_path = path / "__init__.py"

    if not init_path.exists():
        logging.error(f"Extension package '{path}' does not contain __init__.py, skip.")
        return

    unique_id = str(uuid.uuid4()).replace('-', '_')[:8]
    module_name = f'sgs_extension_{unique_id}'

    spec = util.spec_from_file_location(module_name, init_path)
    module = util.module_from_spec(spec)

    assert module_name not in sys.modules
    sys.modules[module_name] = module   # Handle relative imports in the extension.

    spec.loader.exec_module(module)

    get_extension_func = getattr(module, "get_extension", None)
    if get_extension_func is None:
        logging.error(f"Extension package '{path}' does not contain `get_extension` function, skip.")
        return

    try:
        extension = get_extension_func()
        add_extension(extension)
    except Exception:
        from traceback import format_exc
        logging.error(f"Failed to load extension from '{path}'.")
        logging.exception("Error:")
    else:
        logging.info(f"Successfully loaded extension {extension.id!r} from '{path}'.")


def load_all_extensions():
    """Load all extensions."""

    logging.info('Loading extensions ...')
    for ext_path in BUILTIN_EXTENSION_ROOT.iterdir():
        if not ext_path.is_dir():
            continue
        add_extension_from_path(ext_path)
