#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004
#
#  Copyright (C) 2019 JAZIEL LOPEZ SOFTWARE ENGINEER jlopez.mx
#
#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.
#
#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#   0. You just DO WHAT THE FUCK YOU WANT TO.

import unittest
from unittest.mock import MagicMock
import github
import client


class TestClient(unittest.TestCase):

    repo = None

    def setUp(self):
        """
        :return:
        """

        self.repo = MagicMock(github.Repository)
        self.repo.get_pulls = MagicMock(return_value=unittest.mock.Mock(github.PaginatedList.PaginatedList))

        # mocked calls
        client.authorize(user_token="token", repository="foo")

    def test_authorize_require_token(self):

        with self.assertRaises(ValueError):
            client.authorize()

    def test_authorize_require_repository(self):

        with self.assertRaises(ValueError):
            client.authorize(user_token="foo")

    def test_authorize_valid_invocation(self):
        """
        :return:
        """
        client.authorize(user_token="foo", repository="foo")

    def test_get_open_pull_request_require_repo(self):
        """
        :return:
        """

        with self.assertRaises(ValueError):

            client.get_open_pull_requests(base="master")

    def test_get_open_pull_request_require_base(self):
        """
        :return:
        """
        with self.assertRaises(ValueError):

            client.get_open_pull_requests(repo=self.repo)

    def test_get_open_pull_request_valid_invocation(self):
        """
        :return:
        """
        self.assertTrue(client.get_open_pull_requests(repo=self.repo, base="master"))

    def test_get_open_pull_request_returns_paginated_list_of_pulls_request(self):

        self.assertIsInstance(client.get_open_pull_requests(repo=self.repo, base="master"),
                              github.PaginatedList.PaginatedList)

    def test_get_open_pull_requests_review_requester_correct_invocation(self):
        """
        :return:
        """
        pull_request = MagicMock(github.PullRequest.PullRequest)
        pull_requests = [pull_request, pull_request]

        self.assertIsInstance(client.get_open_pull_requests_requested_reviewers(pull_requests=pull_requests), list)

    def test_get_open_pull_requests_review_requester_require_paginated_list_of_pull_requests(self):
        """
        :return:
        """
        with self.assertRaises(ValueError):
            client.get_open_pull_requests_requested_reviewers()

    def test_filter_requested_reviewer_correct_invocation(self):
        """
        :return:
        """

        results = client.filter_requested_reviewer(elements=[], filter_criteria="foo", by=client.BY_LOGIN_NAME)
        self.assertIsInstance(results, list)

    def test_filter_requested_reviewer_require_elements_to_filter(self):
        """
        :return:
        """
        with self.assertRaises(ValueError):
            client.filter_requested_reviewer(filter_criteria="foo", by=client.BY_LOGIN_NAME)

    def test_filter_requested_reviewer_require_filter_criteria(self):
        """
        :return:
        """
        with self.assertRaises(ValueError):
            client.filter_requested_reviewer(elements=list(), by=client.BY_LOGIN_NAME)

    def test_filter_requested_reviewer_require_filter_by(self):
        """
        :return:
        """
        with self.assertRaises(ValueError):
            client.filter_requested_reviewer(elements=list(), filter_criteria="foo")


if __name__ == "__main__":
    unittest.main()
