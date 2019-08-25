import unittest
from unittest.mock import MagicMock, ANY

import github

import client


class TestClient(unittest.TestCase):

    repo = None

    def setUp(self):
        """
        :return:
        """

        self.repo = MagicMock(github.Repository)
        self.repo.get_pulls = MagicMock(
            return_value=github.PaginatedList.PaginatedList(
                contentClass='PullRequests',
                requester=MagicMock(per_page=30),
                firstUrl=ANY,
                firstParams=ANY))

        # mocked calls
        client.authorize(user_token="token")

    def test_authorize_require_token(self):

        with self.assertRaises(ValueError):
            client.authorize()

    def test_authorize_valid_invocation(self):
        """
        :return:
        """
        # declare mocks
        client.authorize = MagicMock(user_token=None)

        #
        client.authorize(user_token="foo")
        client.authorize(user_token="bar")
        client.authorize(user_token="baz")

        #
        client.authorize.assert_called_with(user_token=ANY)

    def test_get_open_pull_request_require_repo(self):

        with self.assertRaises(ValueError):

            client.get_open_pull_requests(base="master")

    def test_get_open_pull_request_require_base(self):

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

    def test_get_open_pull_requests_review_requester(self):

        """
        :return:
        """
        client.get_open_pull_requests_requested_reviewers()


if __name__ == "__main__":
    unittest.main()
