#!/usr/bin/env bash
#
# Perform static analysis checks and reformat Python code
#
#### SETUP ####################################################################

set -o errexit
set -o errtrace
set -o nounset

# shellcheck disable=SC2154
trap '_es=${?};
    printf "${0}: line ${LINENO}: \"${BASH_COMMAND}\"";
    printf " exited with a status of ${_es}\n";
    exit ${_es}' ERR

DIR_REPO="$(cd -P -- "${0%/*}/.." && pwd -P)"
# https://en.wikipedia.org/wiki/ANSI_escape_code
E0="$(printf "\e[0m")"        # reset
E30="$(printf "\e[30m")"      # black foreground
E31="$(printf "\e[31m")"      # red foreground
E107="$(printf "\e[107m")"    # bright white background

#### FUNCTIONS ################################################################

check_docker() {
    local _msg
    if ! docker compose exec app true 2>/dev/null; then
        _msg='The app container/services is not avaialable.'
        _msg="${_msg}\n       First run \`docker compose up\`."
        error_exit "${_msg}"
    fi
}

error_exit() {
    # Echo error message and exit with error
    echo -e "${E31}ERROR:${E0} ${*}" 1>&2
    exit 1
}

print_header() {
    # Print 80 character wide black on white heading with time
    printf "${E30}${E107}# %-70s$(date '+%T') ${E0}\n" "${@}"
}

#### MAIN #####################################################################

cd "${DIR_REPO}"

check_docker

print_header 'isort'
# shellcheck disable=SC2068
docker compose exec app isort ${@:-.} || true
echo

print_header 'black'
# shellcheck disable=SC2068
docker compose exec app black ${@:-.} || true
echo

print_header 'flake8'
# shellcheck disable=SC2068
docker compose exec app flake8 ${@:-.} || true
echo
