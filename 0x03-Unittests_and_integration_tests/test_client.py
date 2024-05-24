#!/usr/bin/env python3
"""
This module contains the unit tests for the `GithubOrgClient` class from the `client` module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that `GithubOrgClient.public_repos` returns the expected list of repos.

        Use `patch` as a context manager to mock `_public_repos_url`.
        """
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        expected_repos = ["repo1", "repo2", "repo3"]
        mock_get_json.return_value = test_payload
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=property(lambda self: "mock_url")):
            client = GithubOrgClient("test_org")
            repos = client.public_repos()
            self.assertEqual(repos, expected_repos)
            mock_get_json.assert_called_once_with("mock_url")


if __name__ == "__main__":
    unittest.main()
