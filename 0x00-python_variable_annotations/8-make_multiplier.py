#!/usr/bin/env python3

"""Task 8"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the float and multiplier.
    """
    return lambda x: x * multiplier
