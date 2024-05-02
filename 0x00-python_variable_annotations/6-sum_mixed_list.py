#!/usr/bin/env python3
"""Task 6
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    return float(sum(mxd_lst))
