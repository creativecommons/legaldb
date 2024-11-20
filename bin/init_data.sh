#!/bin/bash
#
# Initialize Django application data (!!DANGER!!)
#
set -o errexit
set -o errtrace
set -o nounset

# shellcheck disable=SC2154
trap '_es=${?};
    printf "${0}: line ${LINENO}: \"${BASH_COMMAND}\"";
    printf " exited with a status of ${_es}\n";
    exit ${_es}' ERR

DATA_FILE=dev_data.yaml
# https://en.wikipedia.org/wiki/ANSI_escape_code
E0="$(printf "\e[0m")"        # reset
E30="$(printf "\e[30m")"      # black foreground
E31="$(printf "\e[31m")"      # red foreground
E33="$(printf "\e[33m")"      # yellow foreground
E43="$(printf "\e[43m")"      # yellow background
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


danger_confirm() {
    local _confirm _i _prompt _rand

    printf "${E43}${E30}# %-70s$(date '+%T') ${E0}\n" \
        'Confirmation required'
    echo -e "${E33}WARNING:${E0} this scripts deletes the app data"
    # Loop until user enters random number
    _rand=${RANDOM}${RANDOM}${RANDOM}
    _rand=${_rand:0:4}
    _prompt="Type the number, ${_rand}, to continue: "
    _i=0
    while read -p "${_prompt}" -r _confirm
    do
        if [[ "${_confirm}" == "${_rand}" ]]
        then
            echo
            return
        fi
        (( _i > 1 )) && error_exit 'invalid confirmation number'
        _i=$(( ++_i ))
    done
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

check_docker
danger_confirm

print_header 'Drop and recreate PostgreSQL tables'
docker compose exec app ./manage.py dbshell -- -c "
    DROP SCHEMA public CASCADE;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO postgres, public;
    COMMENT ON SCHEMA public IS 'standard public schema';
    "
echo

print_header 'Django migrate (with syncdb)'
docker compose exec app ./manage.py migrate --run-syncdb
echo

print_header 'Django createsuperuser'
docker compose exec app ./manage.py createsuperuser \
    --username admin --email "$(git config --get user.email)"
echo

print_header 'Django loaddata'
du -h "${DATA_FILE}"
docker compose exec app ./manage.py loaddata --verbosity 3 "${DATA_FILE}"
echo
