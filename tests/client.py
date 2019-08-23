import unittest
from unittest.mock import MagicMock

import github

import client


class TestClient(unittest.TestCase):

    def setUp(self):

        """
        :return:
        """

        client.get_open_pull_requests = MagicMock(repo="foo", base="master", return_value=list())

    def test_authorize_require_token(self):

        """
        :return:
        """
        with self.assertRaises(ValueError):
            client.authorize(user_token=None)

    def test_authorize_with_invalid_token_raises_bad_credentials_exception(self):

        """
        :return:
        """
        with self.assertRaises(github.BadCredentialsException):

            client.authorize(user_token="this-is-not-a-github-token").get_user("foo")

    def test_get_open_pull_request_valid_invoke(self):

        """
        :return:
        """

        self.assertEqual(client.get_open_pull_requests(repo="foo", base="master"), list())


if __name__ == "__main__":
    unittest.main()
