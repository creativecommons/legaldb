# caselaw

Creates a static website of Case Law and Scholarship data frm around the world
based on Google Form responses and manually curated.


## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct
([`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)). By participating in this
project you agree to abide by its terms.


## Workflow

1. Gather information via Google Forms.
2. Copy new responses from Form Responses Google Sheets to the Caselaw -
   Primary Data Google Sheet
3. Review and copy-edit the new responses in the Caselaw - Primary Data Google
   Sheet
4. Update the Repository CSVs - Generated CSVs by running:
    ```shell
    ./scripts/overwrite-data.sh
    ```
5. Commit and push the resulting changes. For example:
    ```shell
    git commit -a -m 'Latest changes'
    git push origin master
    ```
    - Please use a more detailed/specific commit message
6. On the hosting server, pull the latest changes into your clone repository.
7. On the hosting server, build the site and copy it into place by running:
   ```shell
   ./scripts/build.sh
   ```
   - (The script will ask for your password in order to run `sudo` when copying
     the built files into position.)


### Countries

When working with countries, make sure to use the same name for the country in
all the spreadsheets. For the purposes of this project, a "Country" is
something that is named in [World - jVectorMap][jvectorworld]. This means that,
for example, we must use "United Kingdom" rather than "Scotland" or "Wales".

"Jurisdiction" is an option this can be used to more accurately describe th
resource's origin. I (RobM) apologize for this.

[jvectorworld]: http://jvectormap.com/maps/world/world


## Website

- **[CC Case Law Database [Beta]][website]**

[website]: https://labs.creativecommons.org/caselaw/


## Spreadsheets


### Repository CSVs


#### Generated CSVs

Generated CSVs:
- [`jekyll/_data/cases.csv`][datacases]
- [`jekyll/_data/scholarship.csv`][datascholarship]

Notes:
- These are the CSV (Comma Separated Values) format spreadsheets that are used
  to build the site pages.
- Do **not** edit the content of these files. Instead:
  1. Edit the Caselaw - Primary Data - Google Sheet
  2. Run `./scripts/overwrite-data.sh`

[datacases]: jekyll/_data/cases.csv
[datascholarship]: jekyll/_data/scholarship.csv


### Caselaw - Primary Data Google Sheet

Google Sheet:
- [Caselaw - Primary Data][primarysheet]

Notes:
- This is the Google sheet that details are copied to from the Results
  spreadsheets and given editorial attention on.
- There are two sheets: CASES and SCHOLARSHIP
- Do not copy the contributor's name into these if they have not selected the
  option to receive credit.
- When a given entry is ready to be published, set the value of the "Publish"
  column to "Publish" for it. Otherwise leave it blank or set it to "N".
- The Sheet ID is `1Z9IcBgdDYoeZw0Xx573ZMp5JcJDCNhOUHrj0guU9byo`. If this
  changes, update the `SHEET_ID` in `./scripts/overwrite-data.sh`.

[primarysheet]: https://docs.google.com/spreadsheets/d/1Z9IcBgdDYoeZw0Xx573ZMp5JcJDCNhOUHrj0guU9byo/edit#


### Google Form Responses Google Sheets

Google Sheets:
- [Caselaw - Cases Form Responses (for copying from, do not edit)][sheetcases]
- [Caselaw - Scholarship Form Responses (for copying from, do not edit)][sheetscholar]

Notes:
- These Google Sheets are the results of people completing the Google Forms.
- Pay special attention to whether the contributor has selected the option to
  receive credit or not


[sheetcases]: https://docs.google.com/spreadsheets/d/1bd21-MXfGLaWOhUDOCKmGlBDqxzpxr_FZSf_Bpnl_ZI/edit#
[sheetscholar]: https://docs.google.com/spreadsheets/d/1rGo8vOIwUD84YAbvmP0M4k53wSsboUPdeBYKo5vtNzI/edit#gid=284152088


#### Manually Managed CSV

Manually Managed CSV:
- [`jekyll/_data/country.csv`][datacountry]

Notes:
- This is the list of countries we have data for. If a country is not listed
  here, its data will not be used.
- `code` column contains the uppercase two-letter code for the country (ISO
   3166-1 alpha-2). See [World - jVectorMap][jvectorworld].
- `country` column contains the name of the country in English. It must be
   from [World - jVectorMap][jvectorworld]
- `notes` column contains optional text to be included in the country page.

[datacountry]: jekyll/_data/country.csv


## Forms

- [Creative Commons Case Law Database [beta] - Cases][formcases]
- [Creative Commons Case Law Database [beta] - Scholarship][formscholar]

[formcases]: https://docs.google.com/forms/d/e/1FAIpQLSdyhi06rJzP3fnyCfv-d40Q5ucaWRRsaC74G8qlY23xDhspwA/viewform
[formscholar]: https://docs.google.com/forms/d/e/1FAIpQLSfxxk5FWZCl3QURJqF42-FtMoWrwj1PMsdOyk2hUayU7FPB7w/viewform


## Errors


### NoMethodError

Error text:
```
caselaw/jekyll/_plugins/data_page_generator.rb:45:in `eval': undefined method `tr' for nil:NilClass (NoMethodError)
```

You have probably missed out the 'Country' entry for one of the rows in the
spreadsheet.

This error indicates that a value being used in a `dir:` entry for `page_gen:`
in `_config_yml` cannot be found. As we use `data["Country"]` in these, if it
cannot be found this will fail.


## Software Used

- [Jekyll • Simple, blog-aware, static sites | Transform your plain text into
  static websites and blogs](https://jekyllrb.com/)
- [avillafiorita/jekyll-datapage_gen: Generate one page per yaml record in
  Jekyll sites.](https://github.com/avillafiorita/jekyll-datapage_gen)
- [jVectorMap](http://jvectormap.com/)


## Future Work

The following potential work has been identified:
1. Remove the Caselaw - Primary Data Google Sheet cut and paste process. Instead
   manipulate the data in the Google Form Responses Google Sheets.
2. Schedule updates so that a tech person does not need to be wrangled to apply
   updates.


## License

- [`LICENSE`](LICENSE) (Expat/[MIT][mit] License)


[mit]: http://www.opensource.org/licenses/MIT "The MIT License | Open Source Initiative"
