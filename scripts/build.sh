#!/bin/bash
RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
pushd "${RRDIR}"
git pull
pushd jekyll
jekyll build
sudo mkdir -p /var/www/reversionary-rights
sudo cp -r _site/* /var/www/reversionary-rights/
sudo chown -R www-data:www-data /var/www/reversionary-rights/
popd
popd
