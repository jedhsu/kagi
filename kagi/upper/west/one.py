"""

    *Upper-West 1*   |⠁|

  The upper-west one gi.

"""

from dataclasses import dataclass

from kagi import Gi
from ..._gi import StrismicGi
from kagi.import WesternGi
from ..._number import OneGi
from .._gi import UpperGi

__all__ = ["UpperWest1"]


@dataclass
class Ka(
    Western,
    Upper,
    Yikagi,
):
    symbol = "\u2801"
