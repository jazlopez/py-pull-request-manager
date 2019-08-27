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

from github import Github

# client using github api v3

# int constants
AUTHORIZED_USER = 0
AUTHORIZED_REPOSITORY = 1
BY_LOGIN_NAME = 2

# string constants
PULL_REQUEST_EVENT_APPROVE = 'APPROVE'
PULL_REQUEST_EVENT_REQUEST_CHANGES = 'REQUEST_CHANGES'
PULL_REQUEST_EVENT_COMMENT = 'COMMENT'

def authorize(user_token=None, repository=None, returned_value=None):

    """
    :param user_token:
    :param repository:
    :param returned_value:
    :return:
    """

    if not user_token:
        raise ValueError("you must provide user token")

    if not repository:
        raise ValueError("you must provide a repository to read pull requests from")

    authentication = Github(login_or_token=user_token)

    if returned_value is AUTHORIZED_REPOSITORY:
        return authentication.get_repo(repository)

    return authentication


def get_open_pull_requests(repo=None, base=None):

    """
    retrieve open pull requests from specified repository
    :param repo:
    :param base:
    :return github.PaginatedList.PaginatedList
    """

    if not repo:
        raise ValueError("you must provide repo")

    if not base:
        raise ValueError("you must provide base branch")

    return repo.get_pulls(state='open', sort='created', base=base)


def get_open_pull_requests_requested_reviewers(pull_requests=None):

    """
    retrieve requested reviewers from given pull request(s)
    :param pull_requests:
    :return list:
    """

    result = list()

    if not pull_requests:
        raise ValueError("you must provide a paginated list of pull requests")

    for pull_request in pull_requests:
        user_review_requests = pull_request.get_review_requests()[0]
        # teams_review_requests = pull.request.get_review_requests()[1]

        reviewers = [user for user in user_review_requests]

        result.append({
            "users": reviewers,
            "pull_request": {
                "id": pull_request.id,
                "number": pull_request.number,
                "url": pull_request.url,
                "title": pull_request.title
            }
        })

    return result


def filter_requested_reviewer(elements=None, filter_criteria=None, by=None):

    """
    retrieve pull request belonging to given login name
    :param elements:
    :param filter_criteria:
    :param by:
    :return list:
    """

    result = []

    if elements is None:
        raise ValueError("elements to filter must be provided")

    if not filter_criteria:
        raise ValueError("filter criteria must be provided")

    if not by:
        raise ValueError("filter by must be provided")

    if by is not BY_LOGIN_NAME:
        raise ValueError("unknown filter by" % by)

    for data in elements:
        for user in data["users"]:
            if user.login == filter_criteria:
                result.append(data)

    return result


def get_pull_request(pull_request_number=None, repo=None):
    """
    get pull request from given identifier
    :param pull_request_number:
    :param repo:
    :return:
    """
    if not pull_request_number:
        raise ValueError("you must provide pull request number")

    if not repo:
        raise ValueError("you must provide repo")

    return repo.get_pull(pull_request_number)


def approve_pull_request(pull_request=None, body_or_reason=None):
    """
    :param pull_request:
    :param body_or_reason:
    :return:
    """

    if not pull_request:
        raise ValueError("you must provide pull request")

    if not body_or_reason:
        raise ValueError("you must provide approval comment(s)")

    return pull_request.create_review(event=PULL_REQUEST_EVENT_APPROVE, body=body_or_reason)


def comment_pull_request(pull_request=None, body_or_reason=None):
    """
    :param pull_request:
    :param body_or_reason:
    :return:
    """

    if not pull_request:
        raise ValueError("you must provide pull request")

    if not body_or_reason:
        raise ValueError("you must provide comment(s)")

    return pull_request.create_review(event=PULL_REQUEST_EVENT_COMMENT, body=body_or_reason)


def request_changes_pull_request(pull_request=None, body_or_reason=None):
    """
    :param pull_request:
    :param body_or_reason:
    :return:
    """

    if not pull_request:
        raise ValueError("you must provide pull request")

    if not body_or_reason:
        raise ValueError("you must provide request changes comment(s)")

    return pull_request.create_review(event=PULL_REQUEST_EVENT_REQUEST_CHANGES, body=body_or_reason)


__author__ = "Jaziel Lopez at jlopez.m x"