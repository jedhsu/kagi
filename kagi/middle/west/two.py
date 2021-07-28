"""

    *Ki*   |⠅|

  Geometrically, middle-west two.

"""

from dataclasses import dataclass

from kagi._index import I
from ._k import K

__all__ = ["Ki"]


@dataclass
class Ki(
    K,
    I,
):
    symbol = "\u2805"
