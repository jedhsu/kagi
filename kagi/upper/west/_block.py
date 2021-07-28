"""

    *Upper-West Block*   ⠨

  The upper-west block kagi.

"""

from dataclasses import dataclass

from kagi import Kagi
from kagi._hemisphere import WesternKagi
from ..._number import BlockGi
from .._gi import UpperGi

__all__ = ["UpperWestBlock"]


@dataclass
class UpperWestBlock(
    Gi,
    StrismicGi,
    UpperGi,
    WesternGi,
    BlockGi,
):
    pass
