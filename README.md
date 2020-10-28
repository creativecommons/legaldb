# caselaw

<p align="center">
    <a href="https://github.com/creativecommons/caselaw/blob/master/LICENSE"><img alt="MIT license" src="https://img.shields.io/github/license/creativecommons/vocabulary.svg?color=brightgreen"/></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

Curated repository of Case Law and Scholarship data from around the world in a
Django based website.

> :warning:  **This project, CC’s Legal Database, is undergoing
> reimplementation using Django.**
> - [Heroku Dev Site][herokudev]
> - [`develop`][devbranch] branch
> - [Posts in the Outreachy May 2020 round: CC Legal Database
>   series][blogseries]

[herokudev]: https://cc-caselaw.herokuapp.com/
[devbranch]: https://github.com/creativecommons/caselaw/tree/develop
[blogseries]: https://opensource.creativecommons.org/blog/entries/legal-database-a-new-beginning/#series


## Code of Conduct

Please note that this project is released with a Contributor [Code of
Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to
abide by its terms.


## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). It contains some general instructions
that should be followed when contributing to any of the Creative Commons
open-source repositories.


### Development setup

To follow these instructions, Python 3 and
[Pipenv](https://pipenv.pypa.io/en/latest/) are required.

Install dependencies with pipenv.
```shell
pipenv install --dev
```

Copy `.env.template` and set environment variables (like
`DJANGO_DEBUG_ENABLED=True` for local development and testing) and secret keys
in a `.env` file.
```shell
cp .env.template .env
```

After setting variables run the migrations to create the database (we use
Postgresql in this case).
```shell
pipenv run python manage.py migrate
```

The next step is to create an admin account for Django admin.
```shell
pipenv run python manage.py createsuperuser
```

Finally you can start a development server with:
```shell
pipenv run python manage.py runserver
```
and see a local version of the website following `http://127.0.0.1:8000/` on
the browser.

After made code changes and before commit, check code style.
```shell
pipenv run black .
pipenv run flake8
```


## Legacy Information

**The following information is deprecated and will be removed once the
production site is live.**

Visit the legacy website: [CC Legal Database [Beta]][website]

[website]: https://labs.creativecommons.org/caselaw/


### Spreadsheets


#### Caselaw - Primary Data Google Sheet

Google Sheet:
- [Caselaw - Primary Data][primarysheet]

[primarysheet]: https://docs.google.com/spreadsheets/d/1Z9IcBgdDYoeZw0Xx573ZMp5JcJDCNhOUHrj0guU9byo/edit#


#### Google Form Responses Google Sheets

Google Sheets:
- [Caselaw - Cases Form Responses (for copying from, do not edit; Restricted
  Access)][sheetcases]
- [Caselaw - Scholarship Form Responses (for copying from, do not edit;
  Restricted Access)][sheetscholar]

Note: These Google Sheets are the results of people completing the Google
Forms.

[sheetcases]: https://docs.google.com/spreadsheets/d/1bd21-MXfGLaWOhUDOCKmGlBDqxzpxr_FZSf_Bpnl_ZI/edit#
[sheetscholar]: https://docs.google.com/spreadsheets/d/1rGo8vOIwUD84YAbvmP0M4k53wSsboUPdeBYKo5vtNzI/edit#gid=284152088


### Forms

- [Creative Commons Legal Database -- Cases][formcases]
- [Creative Commons Legal Database -- Scholarship][formscholar]

[formcases]: https://docs.google.com/forms/d/e/1FAIpQLSdyhi06rJzP3fnyCfv-d40Q5ucaWRRsaC74G8qlY23xDhspwA/viewform
[formscholar]: https://docs.google.com/forms/d/e/1FAIpQLSfxxk5FWZCl3QURJqF42-FtMoWrwj1PMsdOyk2hUayU7FPB7w/viewform


## License

- [`LICENSE`](LICENSE) (Expat/[MIT][mit] License)

[mit]: http://www.opensource.org/licenses/MIT "The MIT License | Open Source Initiative"
