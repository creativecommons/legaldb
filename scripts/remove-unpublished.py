#!/usr/bin/env python3

import csv
import shutil
import sys
import tempfile

infilename = sys.argv[1]

countries = set()

with open(infilename, newline='') as infile:
    csvreader = csv.DictReader(infile)
    with tempfile.NamedTemporaryFile(mode='w', newline='') as outfile:
        tmpnam = outfile.name
        csvwriter = csv.DictWriter(outfile, fieldnames=csvreader.fieldnames)
        csvwriter.writeheader()
        for row in csvreader:
            if row['Publish'] in ['Y', 'y', 'Publish', 'publish']:
                # Remove trailing whitespace in country fields, as we use
                # the country directly as a key.
                row['Country'] = row['Country'].strip()
                csvwriter.writerow(row)
                countries.add(row['Country'])
        shutil.copy(tmpnam, infilename)

print("Countries mentioned in " + infilename + ":")
print("\n".join(sorted(countries)))
