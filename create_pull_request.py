import argparse
import logging
from settings import GITHUB_USER_TOKEN
from client import authorize, create_pull_request, AUTHORIZED_REPOSITORY

parser = argparse.ArgumentParser(description="")
parser.add_argument("--title", required=True, help="Pull Request Title")
parser.add_argument("--description", required=True, help="Pull Request Description")
parser.add_argument("--repository", required=True, help="Repository pull request")
parser.add_argument("--head", required=True, help="Branch name of your implemented changes")
parser.add_argument("--base", required=True, help="Branch name to merge your changes into")

args = parser.parse_args()
GITHUB_TITLE_PULL_REQUEST = args.title
GITHUB_DESCRIPTION_PULL_REQUEST = args.description
GITHUB_HEAD_PULL_REQUEST = args.head
GITHUB_BASE_PULL_REQUEST = args.base
GITHUB_REPOSITORY = args.repository

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

logging.info("# signing in...asking for repository access using provided user token...")
logging.info("# repository connection details")
logging.info("# \trepository: {}".format(GITHUB_REPOSITORY))
logging.info("# \thead branch: {}".format(GITHUB_HEAD_PULL_REQUEST))
logging.info("# \tbase branch: {}".format(GITHUB_BASE_PULL_REQUEST))

repository = authorize(user_token=GITHUB_USER_TOKEN, repository=GITHUB_REPOSITORY, returned_value=AUTHORIZED_REPOSITORY)
logging.info("# authorization repository access allowed")

try:
    response = create_pull_request(
        repo=repository,
        title=GITHUB_TITLE_PULL_REQUEST,
        description=GITHUB_DESCRIPTION_PULL_REQUEST,
        base=GITHUB_BASE_PULL_REQUEST,
        head=GITHUB_HEAD_PULL_REQUEST)

    logging.info("# Created Pull Request")
    logging.info("# Pull Request %d: %s", response.number, response.title)
    logging.info("# Pull Request URL %s:", response.html_url)

except RuntimeError as e:
    logging.error(e)
