#!/bin/bash
# =====================================================================
# Description: configure .env file from command line
# Author: Jaziel Lopez jlopez.mx
# Date: 2019
#  ./env.provision.credentials.sh
# =====================================================================

set -e

GITHUB_LOGIN_NAME=""
GITHUB_USER_TOKEN=""
CONFIRM_RETRY=""
function do_provision_credentials() {
    printf "\n"
    printf "Interactive Configure Github Credentials\n\n"

    echo "  This program will manage pull requests by connecting to Github on your behalf. "
    echo "  For more information see the link below:"
    echo "  https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line"
    echo ""
    read -p "> Enter your Github Login Name: " GITHUB_LOGIN_NAME
    read -p "> Enter your Github User Token: " GITHUB_USER_TOKEN
    read -p "Press [C] to confirm or [R] to reset values: " CONFIRM_RETRY
}

function do_provision_env_file() {

    if [[ -f .env ]]; then
        cp ./.env ./.env.old
    fi

    rm -f .env

    IFS=''
    while read LINE; do echo "# $LINE" >> ./.env; done < ./LICENSE.md
    echo "" >> ./.env
    echo "GITHUB_USER_TOKEN=$GITHUB_USER_TOKEN" >> ./.env
    echo "GITHUB_LOGIN_NAME=$GITHUB_LOGIN_NAME" >> ./.env
    echo "" >> ./.env
    echo "--"
    echo ".env file has been configured successfully"
    echo "Completed Installation"
    exit 0
}


do_provision_credentials

while [[ True ]]; do

    case ${CONFIRM_RETRY} in
        r|R)
            do_provision_credentials;;
        c|C)
            do_provision_env_file ; exit 0;;
        *)
            echo "Invalid entry"
            read -p "Press [C] to confirm or [R] to reset values: " CONFIRM_RETRY
    esac
done