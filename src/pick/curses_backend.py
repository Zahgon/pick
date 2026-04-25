import curses
from typing import Optional, Tuple

from .backend import Backend


class CursesBackend(Backend):
    """Backend that uses the curses standard library."""

    def __init__(self, screen: Optional["curses._CursesWindow"] = None) -> None:
        self._screen = screen

    def setup(self) -> None:
        pass

    def teardown(self) -> None:
        pass  # curses.wrapper handles cleanup

    def clear(self) -> None:
        pass

    def getmaxyx(self) -> Tuple[int, int]:
        pass

    def addnstr(self, y: int, x: int, s: str, n: int) -> None:
        pass

    def getch(self) -> int:
        pass

    def refresh(self) -> None:
        pass
