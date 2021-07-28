"""

    *Upper-West 2*   |⠃|

  The upper-west two gi.

"""

from dataclasses import dataclass

from kagi import Kagi
from kagi import WesternKagi
from ..._number import TwoGi
from .._gi import UpperGi

__all__ = ["UpperWest2"]


@dataclass
class UpperWest2(
    Kagi,
    UpperGi,
    WesternGi,
    TwoGi,
):
    symbol = "\u2803"
