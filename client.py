from github import Github

# client using github api v3


def authorize(user_token=None):

    """
    :param user_token:
    :return:
    """
    return Github(login_or_token=user_token)


def get_open_pull_requests(repo=None, base=None):

    """
    :param repo:
    :param base:
    :return:
    """

    return repo.get_pulls(state='open', sort='created', base=base)


__author__ = "Jaziel Lopez at jlopez.mx"