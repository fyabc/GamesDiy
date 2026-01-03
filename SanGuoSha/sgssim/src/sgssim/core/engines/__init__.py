#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import json
from typing import Optional

from .engine import BaseEngine


def create_engine_from_config(config_str: str, seed: Optional[int] = None) -> BaseEngine:
    """Create an engine from config."""

    # Load from builtin.
    if config_str.startswith('builtin:'):
        _, mode, mode_config_str = config_str.split(':', 2)
        if mode.lower() in ('rp', 'roleplay'):
            from .roleplay import RolePlayEngine, BUILTIN_RP_CONFIGS

            config = BUILTIN_RP_CONFIGS.get(mode_config_str, None)
            if config is None:
                raise ValueError(f"Unknown builtin roleplay config: {mode_config_str}")
            return RolePlayEngine(config, seed)
        else:
            raise ValueError(f"Unknown builtin mode: {mode}")

    # Load from JSON.
    with open(config_str, 'r', encoding='utf-8') as f_conf:
        config = json.load(f_conf)
        mode = config['mode']
        if mode.lower() in ('rp', 'roleplay'):
            from .roleplay import RolePlayEngine
            return RolePlayEngine(config, seed)
        else:
            raise ValueError(f"Unknown mode: {mode}")
