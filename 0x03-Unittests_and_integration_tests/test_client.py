#!/usr/bin/env python3
"""
This module contains the unit tests for the `GithubOrgClient` class from the `client` module.
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "mock_org"})
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that `GithubOrgClient.org` returns the correct value.

        Parameters:
        - org_name: the name of the organization.
        - expected: the expected result.
        - mock_get_json: the mocked `get_json` method.
        """
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org_name))
        self.assertEqual(result, {"login": "mock_org"})

    def test_public_repos_url(self):
        """
        Test that `GithubOrgClient._public_repos_url` returns the expected URL.

        Use `patch` as a context manager to mock the `org` property.
        """
        expected_repos_url = "https://api.github.com/orgs/test_org/repos"
        with patch.object(GithubOrgClient, 'org', new_callable=property(lambda self: {"repos_url": expected_repos_url})):
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url, expected_repos_url)


if __name__ == "__main__":
    unittest.main()
