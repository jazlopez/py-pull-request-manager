from github import Github

# client using github api v3

AUTHORIZED_USER = 0
AUTHORIZED_REPOSITORY = 1
BY_LOGIN_NAME = 2

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
    :param repo:
    :param base:
    :return:
    """

    if not repo:
        raise ValueError("you must provide repo")

    if not base:
        raise ValueError("you must provide base branch")

    return repo.get_pulls(state='open', sort='created', base=base)


def get_open_pull_requests_requested_reviewers(pull_requests=None):

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
                "url": pull_request.url,
                "title": pull_request.title
            }
        })

    return result


def filter_requested_reviewer(elements=None, filter_criteria=None, by=None):

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


__author__ = "Jaziel Lopez at jlopez.mx"