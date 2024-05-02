#!/usr/bin/env python3
"""Task 1
"""

from typing import TypeVar, Dict, Any


K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: V = None) -> V:
    """
    Returns the value corresponding to the given key in the
    dictionary, or the default value if the key is not found.

    Args:
        dct (Dict[K, V]): The input dictionary.
        key (K): The key to look up in the dictionary.
        default (V, optional): The default value to return if
        the key is not found. Defaults to None.

    Returns:
        V: The value corresponding to the key in the dictionary, or
        the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
