#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

"""Clean-up CSV file and list countries referenced.
"""

# Standard library
import csv
import os.path
import shutil
import sys
import tempfile


infilename = sys.argv[1]

countries = set()

with open(infilename, newline="") as infile:
    csvreader = csv.DictReader(infile)
    with tempfile.NamedTemporaryFile(mode="w", newline="") as outfile:
        tmpnam = outfile.name
        csvwriter = csv.DictWriter(outfile, fieldnames=csvreader.fieldnames,
                                   lineterminator="\n")
        csvwriter.writeheader()
        for row in csvreader:
            if row["Publish"].strip() in ["Y", "y", "Publish", "publish"]:
                # Strip leading/trailing whitespace from all columns. This is
                # especially important for the country column, as we use the
                # country value as a key.
                for key in row.keys():
                    row[key] = row[key].strip()
                row["Country"] = row["Country"].strip()
                csvwriter.writerow(row)
                countries.add("  {}".format(row["Country"]))
        shutil.copy(tmpnam, infilename)

print("Countries referenced in " + os.path.basename(infilename) + ":")
print("\n".join(sorted(countries)))
