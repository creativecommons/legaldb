# Workflow

1. Gather information via Google Forms.
2. Review and copy-edit that information in the "Master Spreadsheet" Google Sheet.
3. Note the Google Sheets Document ID. for the Master Spreadsheet. e.g. for the sheet: `https://docs.google.com/spreadsheets/d/`1436GBvNkSCQ3uRR7ZLPUDEZH2rknvuD7ZJ7vFGhWgoM/edit` the id is `1436GBvNkSCQ3uRR7ZLPUDEZH2rknvuD7ZJ7vFGhWgoM`.
4. Update the data in jekyll/_data by running `./scripts/overwrite-data.sh` with the sheet ID as its argument. e.g. `./scripts/overwrite-data.sh 1436GBvNkSCQ3uRR7ZLPUDEZH2rknvuD7ZJ7vFGhWgoM` .
5. Commit the resulting changes to git, e.g. `git commit -a -m "Latest changes"` . Then push them, e.g. `git push origin master` .
6. On the server, fetch the latest changes using `git pull`.
7. Build the site and copy it into place by running `./scripts/build.sh` . This will ask for your password in order to run `sudo` when copying the built files into position.

When working with countries, make sure to use the same name for the country in
all the spreadsheets. For the purposes of this project, a "Country" is something that is named in http://jvectormap.com/maps/world/world , mentioned below. This means that (for example) we must use "United Kingdom" rather than "Scotland" or "Wales". Where "Jurisdiction" is an option this can be used to more accurately describe the resource's origin. I (RobM) apologize for this. 

# Spreadsheets

There are two sets of spreadsheets

## Google Form Results

These are the results of people completing the Google Forms. Pay special
attention to whether the contributor has selected the option to receive credit
or not

## "Master Spreadsheet" Google Sheet

This is the Google sheet that details are copied to from the Results
spreadsheets and given editorial attention on.

Do not copy the contributor's name into these if they have not selected the
option to receive credit.

When a given entry is ready to be published, set the value of the "Publish" column to "Publish" for it. Otherwise leave it blank or set it to "N".

## CSV Documents in _data

These are the CSV (Comma Separated Values) format spreadsheets in `jekyll/_data`
that we use to build the pages.

Apart from countries.csv, do not edit the content of these files, rather edit
the Google Sheet then run `./scripts/overwrite-data.sh` .

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

# Errors

## caselaw/jekyll/_plugins/data_page_generator.rb:45:in `eval': undefined method `tr' for nil:NilClass (NoMethodError)

You have probably missed out the 'Country' entry for one of the rows in the spreadsheet.

(This error indicates that a value being used in a `dir:` entry for `page_gen:` in `_config_yml` cannot be found. As we use `data["Country"]` in these, if it cannot be found this will fail.)

# Used Software

https://jekyllrb.com/

https://github.com/avillafiorita/jekyll-datapage_gen

http://jvectormap.com/
