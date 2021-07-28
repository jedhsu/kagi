"""

    *Ka*   |⠂|

  Geometrically, middle-west one.

"""

from dataclasses import dataclass

from kagi._index import A
from ._k import K

__all__ = ["Ka"]


@dataclass
class Ka(
    K,
    A,
):
    symbol = "\u2802"
