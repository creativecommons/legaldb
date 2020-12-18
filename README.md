# legaldb

<p align="center">
    <a href="https://github.com/creativecommons/caselaw/blob/master/LICENSE"><img alt="MIT license" src="https://img.shields.io/github/license/creativecommons/vocabulary.svg?color=brightgreen"/></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

CC Legal Database: curated repository of Case Law and Scholarship data from around the world in a Django based website.

**[legaldb.creativecommons.org](https://legaldb.creativecommons.org/)**


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

Open another terminal and navigate to webpack folder using:
```shell
cd webpack
```

To install webpackdependencies with:
```shell
npm install
```

If you want to make changes to scss files during development run:
```shell
npm run watch
```

otherwise run the following command
```shell
npm run build
```

After made code changes and before commit, check code style from main directory using.
```shell
pipenv run black .
pipenv run flake8
```


### Development Blog Posts

[Posts in the Outreachy May 2020 round: CC Legal Database series][blogseries]

[blogseries]: https://opensource.creativecommons.org/blog/entries/legal-database-a-new-beginning/#series


## Deploy to Heroku

See [`deploy_to_heroku.md`](deploy_to_heroku.md).


## License

- [`LICENSE`](LICENSE) (Expat/[MIT][mit] License)

[mit]: http://www.opensource.org/licenses/MIT "The MIT License | Open Source Initiative"
