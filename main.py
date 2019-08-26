# main.py

from settings import GITHUB_REPOSITORY, GITHUB_USER_TOKEN, GITHUB_BASE_PULL_REQUEST
from client import authorize, get_open_pull_requests, \
    get_open_pull_requests_requested_reviewers, \
    approve_pull_request, request_changes_pull_request, \
    comment_pull_request, get_pull_request, filter_requested_reviewer, \
    BY_LOGIN_NAME, AUTHORIZED_REPOSITORY

repository = authorize(user_token=GITHUB_USER_TOKEN, repository=GITHUB_REPOSITORY, returned_value=AUTHORIZED_REPOSITORY)

open_pull_requests = get_open_pull_requests(repo=repository, base=GITHUB_BASE_PULL_REQUEST)

reviewers = get_open_pull_requests_requested_reviewers(pull_requests=open_pull_requests)

filtered = filter_requested_reviewer(elements=reviewers, filter_criteria="foo", by=BY_LOGIN_NAME)

for f in filtered:

    # get reference pull request number
    # pull_request_number = f["pull_request"]["number"]

    # get pull request itself using the reference  number
    # pull_request = get_pull_request(pull_request_number=pull_request_number, repo=repository)

    # request changes pull request
    # requested_changes = request_changes_pull_request(pull_request=pull_request, body_or_reason="foo bar baz")

    # approve pull request
    # approved = approve_pull_request(pull_request=pull_request, body_or_reason="foo bar baz")

    # comment only pull request
    # commented = comment_pull_request(pull_request=pull_request, body_or_reason="foo bar baz")
    pass

__author__ = "Jaziel Lopez at jlopez.m x"