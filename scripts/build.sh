#!/bin/bash
#
# Pull the latest changes, build them here, then deploy inside /var/www/
# This hardcodes a lot of assumptions.
set -o errexit
set -o errtrace
set -o nounset

RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
DIR_LIVE=/var/www/caselaw
DIR_OLDBAK=/var/www/_OLDBAK.caselaw

pushd "${RRDIR}" > /dev/null
echo '# git pull'
git pull
echo

if [[ -d ${DIR_OLDBAK} ]]
then
    echo '# removing previous _OLDBAK directory'
    sudo rm -rf ${DIR_OLDBAK}
    echo 'removed.'
    echo
fi

pushd jekyll >/dev/null
echo '# jekyll build'
/usr/local/bin/bundle exec jekyll build \
    --config _config.yml,_config-publish.yml
echo

echo '# copying hosting directory to _OLDBAK directory'
sudo cp -a ${DIR_LIVE} ${DIR_OLDBAK}
echo 'copied.'
echo

echo '# rsyncing built site to hosting directory'
sudo rsync \
    --verbose \
    --checksum \
    --recursive \
    --links \
    --perms \
    --devices \
    --specials \
    --delete-during \
    --delete-excluded \
    --prune-empty-dirs \
    --human-readable \
    --human-readable \
    --human-readable \
    --itemize-changes \
    _site/* /var/www/caselaw/
echo

popd >/dev/null
popd >/dev/null
