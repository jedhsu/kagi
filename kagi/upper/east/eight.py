"""

    *Upper-East 8*

  The upper-east eight gi.

"""

from dataclasses import dataclass

from ...._gi import Kagi
from ..._gi import StrismicKagi
from ...east import EasternKagi
from ..._number import EightKagi
from .._gi import UpperKagi

__all__ = ["UpperEast8"]


@dataclass
class UpperEast8(
    Kagi,
    StrismicKagi,
    UpperKagi,
    EasternKagi,
    EightKagi,
):
    symbol = "\u2828"
