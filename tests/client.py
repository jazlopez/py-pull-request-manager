import unittest
from unittest.mock import MagicMock, ANY

import client


class TestClient(unittest.TestCase):

    def setUp(self):

        """
        :return:
        """
        # declare mocks
        client.authorize = MagicMock(user_token=None)
        client.get_open_pull_requests = MagicMock(repo=None, base=None)

        # actual calls
        client.authorize(user_token="token")
        client.get_open_pull_requests(repo="foo", base="master")

    def test_authorize_valid_invocation(self):

        """
        :return:
        """
        client.authorize.assert_called_with(user_token=ANY)

    def test_get_open_pull_request_valid_invocation(self):

        """
        :return:
        """
        client.get_open_pull_requests.assert_called_with(repo=ANY, base=ANY)


if __name__ == "__main__":
    unittest.main()
