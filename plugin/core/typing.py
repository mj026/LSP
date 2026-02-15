from __future__ import annotations

from enum import Enum  # noqa: F401
from enum import IntEnum  # noqa: F401
from enum import IntFlag  # noqa: F401
from typing import Any  # noqa: F401
from typing import Callable  # noqa: F401
from typing import cast  # noqa: F401
from typing import Deque  # noqa: F401
from typing import Dict  # noqa: F401
from typing import final  # noqa: F401
from typing import Generator  # noqa: F401
from typing import Generic  # noqa: F401
from typing import IO  # noqa: F401
from typing import Iterable  # noqa: F401
from typing import Iterator  # noqa: F401
from typing import List  # noqa: F401
from typing import Literal  # noqa: F401
from typing import Mapping  # noqa: F401
from typing import Optional  # noqa: F401
from typing import Protocol  # noqa: F401
from typing import Sequence  # noqa: F401
from typing import Set  # noqa: F401
from typing import Tuple  # noqa: F401
from typing import Type  # noqa: F401
from typing import TYPE_CHECKING  # noqa: F401
from typing import TypedDict  # noqa: F401
from typing import TypeVar  # noqa: F401
from typing import Union  # noqa: F401
from typing_extensions import NotRequired  # noqa: F401
from typing_extensions import ParamSpec  # noqa: F401
from typing_extensions import Required  # noqa: F401
from typing_extensions import TypeGuard  # noqa: F401
import sys


if sys.version_info >= (3, 11):
    from enum import StrEnum  # noqa: F401
else:
    class StrEnum(str, Enum):
        """
        Naive polyfill for Python 3.11's StrEnum.

        See https://docs.python.org/3.11/library/enum.html#enum.StrEnum
        """

        __format__ = str.__format__
        __str__ = str.__str__
