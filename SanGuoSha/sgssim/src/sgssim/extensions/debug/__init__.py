#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from pathlib import Path

from sgssim.core.extension import Extension, ExtensionPriority


EXTENSION_ID = "DEBUG"


def get_extension() -> Extension:
    extension = Extension(
        ext_id=EXTENSION_ID,
        ext_root_path=Path(__file__).parent.absolute(),
        priority=ExtensionPriority.DEBUG,
    )

    return extension
