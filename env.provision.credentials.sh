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
    read -p "> Enter your Github Login Name: " GITHUB_LOGIN_NAME
    read -p "> Enter your Github User Token: " GITHUB_USER_TOKEN

    echo "==============================================="
    echo "Github Login Name: $GITHUB_LOGIN_NAME"
    echo "Github User Access Token: $GITHUB_USER_TOKEN"
    echo "==============================================="
    read -p "Press [C] to confirm or [R] to reset values: " CONFIRM_RETRY
}

function do_provision_env_file() {

    if [[ -f .env ]]; then
        cp .env .env.old
    fi

    rm -f .env

    IFS=''
    while read LINE; do echo "# $LINE" >> .env ; done < LICENSE.md

    echo "GITHUB_USER_TOKEN=$GITHUB_USER_TOKEN" >> .env
    echo "GITHUB_LOGIN_NAME=$GITHUB_LOGIN_NAME" >> .env
    echo "==============================================="
    echo ".env file has been configured successfully"
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