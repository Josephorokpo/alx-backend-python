#!/usr/bin/env python3
"""
This module contains the integration tests for the `GithubOrgClient` class from the `client` module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
                     [(org_payload, repos_payload, expected_repos, apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that `GithubOrgClient.public_repos` returns the expected list of repositories.

        Use the example payloads provided in the fixtures.
        """
        # Configure the mock to return the org payload for the org URL
        self.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: self.org_payload),
            unittest.mock.Mock(json=lambda: self.repos_payload)
        ]

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the public_repos method
        repos = client.public_repos()

        # Assert that the result matches the expected list of repositories
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test that `GithubOrgClient.public_repos` returns only repositories with the Apache 2 license.

        Use the example payloads provided in the fixtures.
        """
        # Configure the mock to return the org payload for the org URL
        self.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: self.org_payload),
            unittest.mock.Mock(json=lambda: self.repos_payload)
        ]

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the public_repos method with the license filter
        repos = client.public_repos(license="Apache-2.0")

        # Assert that the result matches the expected list of Apache 2 repositories
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
