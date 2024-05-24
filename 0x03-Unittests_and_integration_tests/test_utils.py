#!/usr/bin/env python3
"""
This module contains the unit tests for the `get_json` function
from the `utils` module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test case for the `get_json` function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test that `get_json` returns the expected result.

        Parameters:
        - test_url: the URL to fetch the JSON data from.
        - test_payload: the expected JSON payload.
        """
        with patch('requests.get') as mocked_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mocked_get.return_value = mock_response

            result = get_json(test_url)
            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
