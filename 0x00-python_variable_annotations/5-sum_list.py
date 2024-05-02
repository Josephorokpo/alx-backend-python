#!/usr/bin/env python3
"""Task 5"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the floats in the list.
    """
    return float(sum(input_list))
