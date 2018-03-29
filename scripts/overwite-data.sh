#!/bin/bash

# Fetch the latest data from Google Docs and overwrite the versions

RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

curl 'https://docs.google.com/spreadsheets/d/1c0VIUgFJYSbtTEZThPyoB-FetMvQDPv7FihrsXi6GwA/export?exportFormat=csv' \
     > "${RRDIR}/jekyll/_data/bills.csv"

curl 'https://docs.google.com/spreadsheets/d/1wtjxgDWgC-jGLVIT1gUpPw9NUzPZa8ShetQlmJWRhnw/export?exportFormat=csv' \
     > "${RRDIR}/jekyll/_data/decisions.csv"

curl 'https://docs.google.com/spreadsheets/d/17G3bnBt-3Bsqw1Ra45kIW8Z4VrhEp2_HhYD13ByfQD4/export?exportFormat=csv' \
    > "${RRDIR}/jekyll/_data/legislation.csv"

curl 'https://docs.google.com/spreadsheets/d/1Or6UcG2OyddsEpO6WQ2H2XFnJs-0EvJJtXoe18QMydI/export?exportFormat=csv' \
     > "${RRDIR}/jekyll/_data/resources.csv"
