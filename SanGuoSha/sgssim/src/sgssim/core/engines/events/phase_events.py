#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from typing import TYPE_CHECKING

from .base import Event
from ..phases import Phase

if TYPE_CHECKING:
    from ...engines import BaseEngine


class PhaseStart(Event):
    """进入某阶段"""

    def __init__(self, phase: Phase):
        self.phase = phase

    def __rich__(self):
        return f"[yellow]PhaseStart({self.phase.value})[/]"

    def happen(self, engine: 'BaseEngine') -> 'list[Event]':
        engine.current_phase = self.phase
        return []


class PhaseEnd(Event):
    """结束某阶段"""

    def __init__(self, phase: Phase):
        self.phase = phase

    def __rich__(self):
        return f"[yellow]PhaseEnd({self.phase.value})[/]"


class PreparePhaseStart(PhaseStart):
    """准备阶段开始"""

    def __init__(self):
        super().__init__(Phase.PREPARE)


class JudgePhaseStart(PhaseStart):
    """判定阶段开始"""

    def __init__(self):
        super().__init__(Phase.JUDGE)


class DrawCardPhaseStart(PhaseStart):
    """摸牌阶段开始"""

    def __init__(self):
        super().__init__(Phase.DRAW_CARD)

    def happen(self, engine: 'BaseEngine') -> 'list[Event]':
        from .card_events import DrawCards

        player_id = engine.current_player_idx
        return [DrawCards(player_id, 2)]


class PlayPhaseStart(PhaseStart):
    """出牌阶段开始"""

    def __init__(self):
        super().__init__(Phase.PLAY)


class DiscardPhaseStart(PhaseStart):
    """弃牌阶段开始"""

    def __init__(self):
        super().__init__(Phase.DISCARD)


class EndPhaseStart(PhaseStart):
    """结束阶段开始"""

    def __init__(self):
        super().__init__(Phase.END)


class PreparePhaseEnd(PhaseEnd):
    """准备阶段结束"""

    def __init__(self):
        super().__init__(Phase.PREPARE)


class JudgePhaseEnd(PhaseEnd):
    """判定阶段结束"""

    def __init__(self):
        super().__init__(Phase.JUDGE)


class DrawCardPhaseEnd(PhaseEnd):
    """摸牌阶段结束"""

    def __init__(self):
        super().__init__(Phase.DRAW_CARD)


class PlayPhaseEnd(PhaseEnd):
    """出牌阶段结束"""

    def __init__(self):
        super().__init__(Phase.PLAY)


class DiscardPhaseEnd(PhaseEnd):
    """弃牌阶段结束"""

    def __init__(self):
        super().__init__(Phase.DISCARD)


class EndPhaseEnd(PhaseEnd):
    """结束阶段结束"""

    def __init__(self):
        super().__init__(Phase.END)
