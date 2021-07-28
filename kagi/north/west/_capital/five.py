"""

    *North-West Capital 5*   ⠨

  The north-west capital five gi.

"""

from dataclasses import dataclass

from ....._gi import Gi
from ....capital import CapitalGi
from ...._gi import StrismicGi
from ....west import WesternGi
from ...._number import FiveGi
from ..._gi import NorthernGi

__all__ = ["NorthWestCapital5"]


@dataclass
class NorthWestCapital5(
    Gi,
    StrismicGi,
    NorthernGi,
    WesternGi,
    CapitalGi,
    FiveGi,
):
    symbol = "\u2828"
