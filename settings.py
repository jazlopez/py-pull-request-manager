import os

# settings module

try:
    from dotenv import load_dotenv

    if not os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))):
        raise FileNotFoundError("expected .env file could not be found")

    load_dotenv(verbose=True, override=True)
except FileNotFoundError or ImportError:
    pass

GITHUB_USER_TOKEN = os.getenv("GITHUB_USER_TOKEN")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY_PULL_REQUEST")
GITHUB_BASE_PULL_REQUEST = os.getenv("GITHUB_BASE_PULL_REQUEST")

__author__ = "Jaziel Lopez at jlopez.mx"
