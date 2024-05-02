#!/usr/bin/env python3
"""Task 9's module.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements from lst and their lengths.

    Args:
        lst (List[str]): The list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple
        contains an element from lst and its length.
    """
    return [(i, len(i)) for i in lst]
