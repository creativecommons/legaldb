#!/bin/bash

# Pull the latest changes, build them here, then deploy inside /var/www/
# This hardcodes a lot of assumptions.

RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

pushd "${RRDIR}"
git pull
pushd jekyll
/usr/local/bin/bundle exec jekyll build \
                      --config _config.yml,_config-publish.yml
sudo -u www-data mkdir -p /var/www/caselaw
sudo -u www-data cp -r _site/* /var/www/caselaw/
popd
popd
