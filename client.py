from github import Github

# client using github api v3


def authorize(user_token=None):

    """
    :param user_token:
    :return:
    """

    if not user_token:
        raise ValueError("you must provide user token")

    return Github(login_or_token=user_token)


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

def get_open_pull_requests_requested_reviewers():
    pass


__author__ = "Jaziel Lopez at jlopez.mx"