import client
import unittest
import github


class TestClient(unittest.TestCase):

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

    def test_get_open_pull_requests_require_repo(self):
        """
        :return:
        """
        with self.assertRaises(ValueError):
            client.get_open_pull_requests(repo=None, base="master")

    def test_get_open_pull_requests_require_base_branch(self):
        """
        :return:
        """
        with self.assertRaises(ValueError):
            client.get_open_pull_requests(repo="foo", base=None)


if __name__ == "__main__":
    unittest.main()
