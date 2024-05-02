#!/usr/bin/env python3
"""Task 12
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the elements of the input tuple by repeating each element
    by a specified factor.

    Args:
        lst (Tuple[Any, ...]): The input tuple of elements to be zoomed in.
        factor (int, optional): The factor by which each element should be
        repeated. Defaults to 2.

    Returns:
        Tuple[Any, ...]: The zoomed-in tuple containing the
        elements repeated by the specified factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
