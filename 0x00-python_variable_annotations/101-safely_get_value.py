#!/usr/bin/env python3
"""Task 11
"""

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Returns the value corresponding to the given key in the
    dictionary, or the default value if the key is not found.

    Args:
        dct (Dict[K, V]): The input dictionary.
        key (K): The key to look up in the dictionary.
        default (V, optional): The default value to return if the
        key is not found. Defaults to None.

    Returns:
        V: The value corresponding to the key in the
        dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
