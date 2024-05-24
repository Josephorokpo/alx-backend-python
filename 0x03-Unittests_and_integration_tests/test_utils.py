#!/usr/bin/env python3
"""
This module contains the unit tests for the `memoize` decorator from the `utils` module.
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test case for the `memoize` decorator."""

    def test_memoize(self) -> None:
        """Test the memoize decorator."""

        class TestClass:
            """Test class with a method and a memoized property."""

            def a_method(self) -> int:
                """A method that returns 42."""
                return 42

            @memoize
            def a_property(self) -> int:
                """A memoized property that returns the result of a_method."""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()
            # Call the memoized property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Verify that the result is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Verify that a_method is only called once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
