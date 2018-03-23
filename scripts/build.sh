#!/bin/bash
RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
pushd "${RRDIR}"
git pull
pushd jekyll
jekyll build
mkdir -p /var/www/reversionary-rights
cp -r _site/* /var/www/reversionary-rights/
chown -R www-data:www-data /var/www/reversionary-rights/
popd
popd
