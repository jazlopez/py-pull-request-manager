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

import argparse
import logging
from settings import GITHUB_USER_TOKEN, GITHUB_LOGIN_NAME
from client import authorize, get_open_pull_requests, \
    get_open_pull_requests_requested_reviewers, \
    approve_pull_request, request_changes_pull_request, \
    comment_pull_request, get_pull_request, filter_requested_reviewer, \
    BY_LOGIN_NAME, AUTHORIZED_REPOSITORY

parser = argparse.ArgumentParser(description="")
parser.add_argument("--review-event", required=True, help="Review event",
                    choices=['approve', 'comment', 'request_changes'])
parser.add_argument("--review-comment", required=True, help="Review comment")
parser.add_argument("--repository", required=True, help="Repository pull request")
parser.add_argument("--base", required=True, help="Base branch")

args = parser.parse_args()
REVIEW_EVENT = args.review_event
REVIEW_COMMENT = args.review_comment
GITHUB_REPOSITORY = args.repository
GITHUB_BASE = args.base

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

logging.info("# signing in...asking for repository access using provided user token...")
logging.info("# repository connection details")
logging.info("# \trepository: {}".format(GITHUB_REPOSITORY))
logging.info("# \tbase branch: {}".format(GITHUB_BASE))


repository = authorize(user_token=GITHUB_USER_TOKEN, repository=GITHUB_REPOSITORY, returned_value=AUTHORIZED_REPOSITORY)
logging.info("# authorization repository access allowed")

logging.info("# fetching open pull requests...")
open_pull_requests = get_open_pull_requests(repo=repository, base=GITHUB_BASE)

logging.info("# fetching open pull requests reviewers...")
reviewers = get_open_pull_requests_requested_reviewers(pull_requests=open_pull_requests)

logging.info("# filter pull requests requiring your review...")
filtered = filter_requested_reviewer(elements=reviewers, filter_criteria=GITHUB_LOGIN_NAME, by=BY_LOGIN_NAME)

if filtered:
   for f in filtered:

        # get reference pull request number
        pull_request_number = f["pull_request"]["number"]

        logging.info("# ------------ PULL REQUEST {}----------------------".format(pull_request_number))

        # get pull request itself using the reference  number
        pull_request = get_pull_request(pull_request_number=pull_request_number, repo=repository)

        if REVIEW_EVENT == "approve":
            # approve pull request
            approved = approve_pull_request(pull_request=pull_request, body_or_reason=REVIEW_COMMENT)
            logging.info("# approved pull request:{}\n# content:{}".format(str(pull_request_number), REVIEW_COMMENT))

        if REVIEW_EVENT == "comment":
            # approve pull request
            approved = comment_pull_request(pull_request=pull_request, body_or_reason=REVIEW_COMMENT)
            logging.info("# comment pull request:{}\n# content:{}".format(str(pull_request_number), REVIEW_COMMENT))

        if REVIEW_EVENT == "request_changes":
            # request changes pull request
            requested_changes = request_changes_pull_request(pull_request=pull_request, body_or_reason=REVIEW_COMMENT)
            logging.info("# requested changes for pull request:{}\n# content:{}"
                         .format(str(pull_request_number),REVIEW_COMMENT))

        logging.info("# --------------------------------------------")

else:

    logging.info("# you do not have any outstanding pull request reviews to address... bye")

__author__ = "Jaziel Lopez at jlopez.m x"
