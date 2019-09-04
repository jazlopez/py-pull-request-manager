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
GITHUB_LOGIN_NAME = os.getenv("GITHUB_LOGIN_NAME")

__author__ = "Jaziel Lopez at jlopez.mx"
