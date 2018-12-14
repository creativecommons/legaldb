#!/bin/bash
set -o errexit
set -o errtrace
set -o nounset

# Fetch the latest data from Google Docs and overwrite the current versions
#
# SHEETID is the Google Sheets identifier for Master Spreadsheet. It can be
# found after "/d/" in the sheet URL and before "/edit"
SHEET_ID='1Z9IcBgdDYoeZw0Xx573ZMp5JcJDCNhOUHrj0guU9byo'


RRDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
SHEEET_ID="${1:-${SHEET_ID}}" # Use SHEET_ID from CLI argument (if present)
EXPORT_URL="https://docs.google.com/spreadsheets/d/${SHEET_ID}/export"
DATA_DIR=${RRDIR}/jekyll/_data

GID=0
echo '# Downloading Caselaw - Primary Data: CASES to cases.csv'
echo "# Sheet ID: ${SHEET_ID}"
echo "# CASES sheet GID: ${GID}"
curl "${EXPORT_URL}?gid=${GID}&exportFormat=csv" > ${DATA_DIR}/cases.csv
echo

GID=1441455659
echo '# Downloading Caselaw - Primary Data: SCHOLARSHIP to scholarship.csv'
echo "# Sheet ID: ${SHEET_ID}"
echo "# SCHOLARSHIP sheet GID: ${GID}"
curl "${EXPORT_URL}?gid=${GID}&exportFormat=csv" > ${DATA_DIR}/scholarship.csv
echo

echo '# Cleaning-up cases.csv'
${RRDIR}/scripts/remove-unpublished.py ${DATA_DIR}/cases.csv
echo

echo '# Cleaning-up scholarship.csv'
${RRDIR}/scripts/remove-unpublished.py ${DATA_DIR}/scholarship.csv
echo

echo '# All processes completed successfully.'
