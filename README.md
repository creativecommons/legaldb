# Workflow

1. Gather information via Google Forms.
2. Review and copy-edit that information in Google Sheets.
3. Export the Google Sheets spreadsheets as CSV (Comma Separated Values)
   spreadsheets, saving them in `jekyll/_data/` in this project.
4. Build the site in `jekyll/` using `jekyll build`.
5. Commit the results to git, e.g. `git commit -a -m "Latest changes"`.
5. Copy the built site to the server using `git pull` and serve the built
   `_site`.

When working with countries, make sure to use the same name for the country in
all the spreadsheets.


# Spreadsheets

There are three sets of spreadsheets

## Google Form Results

These are the results of people completing the Google Forms. Pay special
attention to whether the contributor has selected the option to receive credit
or not

## Google Sheets

These are the Google sheets that details are copied to from the Results
spreadsheets and given editorial attention on.

Do not copy the contributor's name into these if they have not selected the
option to receive credit.

To export data from these sheets, choose the File > Download as >
Comma-separated values (.csv, current sheet).

To move them into position, copy and rename them. e.g.

    Downloads/legislation - Sheet1.csv

should be copied to

    jekyll/_data/legislation.csv

Jekyll doesn't like spaces in names, so we rename the files in this way.

## CSV Documents in _data

These are the CSV (Comma Separated Values) format spreadsheets in `jekyll/_data`
that we use to build the pages.

Apart from countries.csv, do not edit the content of these files, rather edit
the Google Sheets then export them and copy them into position.

## countries.csv

`jekyll/data/countries.csv`

The list of countries we have data for. If a country is not listed here, its
data will not be used.

### code

The uppercase two-letter code for the country (ISO 3166-1 alpha-2).
See http://jvectormap.com/maps/world/world/ .

### country

The name of the country. This should be in English.
See http://jvectormap.com/maps/world/world/ .

### notes

Optional text to be included in the country page.

# Used Software

https://jekyllrb.com/

https://github.com/avillafiorita/jekyll-datapage_gen

http://jvectormap.com/
