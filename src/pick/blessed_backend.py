import contextlib
import curses
from typing import Optional, Tuple

from .backend import Backend


class BlessedBackend(Backend):
    """Backend that uses the blessed library (optional dependency)."""

    def __init__(self) -> None:
        import blessed

        pass

    def setup(self) -> None:
        pass

    def teardown(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def getmaxyx(self) -> Tuple[int, int]:
        pass

    def addnstr(self, y: int, x: int, s: str, n: int) -> None:
        pass

    def getch(self) -> int:
        pass

    def refresh(self) -> None:
        pass  # blessed prints directly, no refresh needed
