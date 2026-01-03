#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ...player import Player
    from ...engines import BaseEngine


class Event:
    def __rich__(self):
        return f"[yellow]{self.__class__.__name__}[/]"

    def happen(self, engine: 'BaseEngine') -> 'list[Event]':
        return []


class Handler:
    # Event types to listen.
    EVENTS: list[type[Event]] = []

    # Process before or after event.
    PROCESS_AFTER: bool = True

    def __init__(self, player: 'Optional[Player]' = None):
        self.player = player

    def process(self, event: Event) -> list[Event]:
        return []
