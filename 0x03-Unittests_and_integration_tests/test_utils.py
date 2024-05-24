#!/usr/bin/env python3
"""
This module contains the unit tests for the `access_nested_map` function from
the `utils` module.
"""

import unittest
from parameterized import parameterized
from typing import Any, Dict, Mapping, Sequence, Tuple
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the `access_nested_map` function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping[str, Any], path: Sequence[str], expected: Any) -> None:
        """
        Test that `access_nested_map` returns the correct value
        for given inputs.

        Parameters:
        - nested_map: a nested dictionary to be accessed.
        - path: a sequence of keys representing the path to the value.
        - expected: the expected value at the given path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
