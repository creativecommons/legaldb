#!/bin/bash

# Fetch the latest data from Google Docs and overwrite the versions

RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

curl 'https://docs.google.com/spreadsheets/d/XXXXXXXX/export?exportFormat=csv' \
     > "${RRDIR}/jekyll/_data/cases.csv"

curl 'https://docs.google.com/spreadsheets/d/XXXXXXXX/export?exportFormat=csv' \
     > "${RRDIR}/jekyll/_data/scholarship.csv"

