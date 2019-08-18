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

    def test_authorize_not_raises_exception_with_token(self):
        """
        :return:
        """
        self.assertIsInstance(client.authorize(user_token="foo"), github.Github)

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

    def test_get_open_pull_requests_not_raises_exception_with_required_parameters(self):

        """
        :return:
        """
        test_client = client.authorize(user_token="foo")
        test_repo = test_client.get_repo("foo")

        self.assertIsInstance(

            client.get_open_pull_requests(repo=test_repo, base="foo"),

            github.PaginatedList.PaginatedList)


if __name__ == "__main__":
    unittest.main()
