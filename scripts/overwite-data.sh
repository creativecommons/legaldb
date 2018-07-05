#!/bin/bash

# Fetch the latest data from Google Docs and overwrite the versions

RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"

if [[ $# -ne 1 ]]; then
    echo "Usage: overwrite-data.sh <SHEETID>"
    echo "       Where SHEETID is the Google Sheets identifier for Master Spreadsheet."
    echo "       This can be found after /d/ in the sheet URL and before /edit ."
    echo "       e.g. 1436GBvNkSCQ3uRR7ZLPUDEZH2rknvuD7ZJ7vFGhWgoM"
    exit 1
fi

SHEETID="${1}"

echo $SHEETID

curl "https://docs.google.com/spreadsheets/d/${SHEETID}/export?exportFormat=csv" \
     > "${RRDIR}/jekyll/_data/cases.csv"

curl "https://docs.google.com/spreadsheets/d/${SHEETID}/export?gid=1441455659&exportFormat=csv" \
     > "${RRDIR}/jekyll/_data/scholarship.csv"

"${RRDIR}/scripts/remove-unpublished.py" "${RRDIR}/jekyll/_data/cases.csv"

"${RRDIR}/scripts/remove-unpublished.py" "${RRDIR}/jekyll/_data/scholarship.csv"
