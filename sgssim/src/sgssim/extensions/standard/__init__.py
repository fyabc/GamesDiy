#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from pathlib import Path

from sgssim.core.extension import Extension, ExtensionPriority

from .cards import Strike, Dodge, Peach, Spirits
from .heroes import get_heroes


EXTENSION_ID = "STANDARD"


def get_extension() -> Extension:
    extension = Extension(
        ext_id=EXTENSION_ID,
        ext_root_path=Path(__file__).parent.absolute(),
        priority=ExtensionPriority.DEBUG,
        card_protos={
            Strike.id: Strike(),
            Dodge.id: Dodge(),
            Peach.id: Peach(),
            Spirits.id: Spirits(),
        },
        heroes=get_heroes(),
    )

    return extension
