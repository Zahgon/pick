import curses
import textwrap
from collections import namedtuple
from dataclasses import dataclass, field
from typing import (
    Any,
    Container,
    Generic,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)

from .backend import Backend
from .blessed_backend import BlessedBackend
from .curses_backend import CursesBackend

__all__ = [
    "Picker",
    "pick",
    "Option",
    "Position",
    "Backend",
    "CursesBackend",
    "BlessedBackend",
    "SYMBOL_CIRCLE_FILLED",
    "SYMBOL_CIRCLE_EMPTY",
]


@dataclass
class Option:
    label: str
    value: Any = None
    description: Optional[str] = None
    enabled: bool = True


KEYS_ENTER = (curses.KEY_ENTER, ord("\n"), ord("\r"))
KEYS_UP = (curses.KEY_UP, ord("k"))
KEYS_DOWN = (curses.KEY_DOWN, ord("j"))
KEYS_SELECT = (curses.KEY_RIGHT, ord(" "))

SYMBOL_CIRCLE_FILLED = "(x)"
SYMBOL_CIRCLE_EMPTY = "( )"

OPTION_T = TypeVar("OPTION_T", str, Option)
PICK_RETURN_T = Tuple[OPTION_T, int]

Position = namedtuple("Position", ["y", "x"])


@dataclass
class Picker(Generic[OPTION_T]):
    options: Sequence[OPTION_T]
    title: Optional[str] = None
    indicator: str = "*"
    default_index: int = 0
    multiselect: bool = False
    min_selection_count: int = 0
    selected_indexes: List[int] = field(init=False, default_factory=list)
    index: int = field(init=False, default=0)
    screen: Optional["curses._CursesWindow"] = None
    position: Position = Position(0, 0)
    clear_screen: bool = True
    quit_keys: Optional[Union[Container[int], Iterable[int]]] = None
    backend: Union[str, Backend] = "curses"

    def __post_init__(self) -> None:
        if len(self.options) == 0:
            raise ValueError("options should not be an empty list")

        if self.default_index >= len(self.options):
            raise ValueError("default_index should be less than the length of options")

        if self.multiselect and self.min_selection_count > len(self.options):
            raise ValueError(
                "min_selection_count is bigger than the available options, you will not be able to make any selection"
            )

        if all(
            isinstance(option, Option) and not option.enabled for option in self.options
        ):
            raise ValueError(
                "all given options are disabled, you must at least have one enabled option."
            )

        self.index = self.default_index
        option = self.options[self.index]
        if isinstance(option, Option) and not option.enabled:
            self.move_down()

    def move_up(self) -> None:
        pass

    def move_down(self) -> None:
        pass

    def mark_index(self) -> None:
        pass

    def get_selected(self) -> Union[List[PICK_RETURN_T], PICK_RETURN_T]:
        """return the current selected option as a tuple: (option, index)
        or as a list of tuples (in case multiselect==True)
        """
        pass

    def get_title_lines(self, *, max_width: int = 80) -> List[str]:
        pass

    def get_option_lines(self) -> List[str]:
        pass

    def get_lines(self, *, max_width: int = 80) -> Tuple[List[str], int]:
        pass

    def draw(self, screen: Backend) -> None:
        """draw the UI on the screen, handle scroll if needed"""
        pass

    def run_loop(
        self, screen: Backend, position: Position
    ) -> Union[List[PICK_RETURN_T], PICK_RETURN_T]:
        pass

    def _resolve_backend(self) -> Backend:
        pass

    def config_curses(self) -> None:
        pass

    def _start(self, screen: "curses._CursesWindow"):
        pass

    def start(self):
        def _curses_main(screen: "curses._CursesWindow"):
            pass

        pass


def pick(
    options: Sequence[OPTION_T],
    title: Optional[str] = None,
    indicator: str = "*",
    default_index: int = 0,
    multiselect: bool = False,
    min_selection_count: int = 0,
    screen: Optional["curses._CursesWindow"] = None,
    position: Position = Position(0, 0),
    clear_screen: bool = True,
    quit_keys: Optional[Union[Container[int], Iterable[int]]] = None,
    backend: Union[str, Backend] = "curses",
):
    pass
