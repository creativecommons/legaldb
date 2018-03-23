#!/bin/bash
RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
pushd "${RRDIR}"
git pull
pushd jekyll
/usr/local/bin/bundle exec jekyll build
sudo -u www-data mkdir -p /var/www/reversionary-rights
sudo -u www-data cp -r _site/* /var/www/reversionary-rights/
popd
popd
