"""

    *Kagi*

  A kagi (Japanese for key) is the atomic unit of the keyboard.

  It uses directional characteristics to identify "key", and
  uses Braille for representation.

"""

from abc import ABCMeta

__all__ = ["Kagi"]


class Kagi:
    __metaclass__ = ABCMeta
