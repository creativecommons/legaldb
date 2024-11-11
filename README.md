# legaldb

<p align="center">
    <a href="https://github.com/creativecommons/caselaw/blob/master/LICENSE"><img alt="MIT license" src="https://img.shields.io/github/license/creativecommons/vocabulary.svg?color=brightgreen"/></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

CC Legal Database: curated repository of Case Law and Scholarship data from
around the world in a Django based website.

**[legaldb.creativecommons.org](https://legaldb.creativecommons.org/)**


## Code of conduct

[`CODE_OF_CONDUCT.md`][org-coc]:
> The Creative Commons team is committed to fostering a welcoming community.
> This project and all other Creative Commons open source projects are governed
> by our [Code of Conduct][code_of_conduct]. Please report unacceptable
> behavior to [conduct@creativecommons.org](mailto:conduct@creativecommons.org)
> per our [reporting guidelines][reporting_guide].

[org-coc]: https://github.com/creativecommons/.github/blob/main/CODE_OF_CONDUCT.md
[code_of_conduct]: https://opensource.creativecommons.org/community/code-of-conduct/
[reporting_guide]: https://opensource.creativecommons.org/community/code-of-conduct/enforcement/


## Contributing

See [`CONTRIBUTING.md`][org-contrib].

[org-contrib]: https://github.com/creativecommons/.github/blob/main/CONTRIBUTING.md


## Development setup

For information on learning and installing the prerequisite technologies for this project, please see [Foundational technologies — Creative Commons Open Source][found-tech].

[found-tech]: https://opensource.creativecommons.org/contributing-code/foundational-tech/

Copy `.env.template` and set environment variables (like
`DJANGO_DEBUG_ENABLED=True` for local development and testing) and secret keys
in a `.env` file.

Please read the comments in the `.env` file for specific instructions to get it to work locally.

```shell
cp .env.template .env
```


### Using docker compose


#### Start (and Build) the Servers

Start Django server (backed by PostgreSQL server ) at
[127.0.0.1:8000](http://127.0.0.1:8000/):
```sh
docker compose up
```


#### Run Migrations

Run the migrations to create database schema (we use Postgresql in this case):
```shell
docker compose exec app ./manage.py migrate
```
**(Required after initial build)**


#### Execute Commands

To execute any commands inside the app docker container, follow this format:

```shell
docker compose exec app ./manage.py DJANGO COMMAND HERE
```
or
```shell
docker compose exec app sh -c "SHELL COMMAND HERE"
```

Examples:
- Create a Super User:
    ```shell
    docker compose exec app ./manage.py createsuperuser
    ```
- Collect static files:
    ```shell
    docker compose exec app ./manage.py collectstatic
    ```
- Compress content:
    ```shell
    docker compose exec app ./manage.py compress
    ```
- Run tests:
    ```shell
    docker compose exec app ./manage.py test
    ```


### Using Pipenv

NOTE: The prefered method is [Using docker compose](#using-docker-compose).

To follow these instructions, Python 3 and
[Pipenv](https://pipenv.pypa.io/en/latest/) are required.

Install dependencies with pipenv.
```shell
pipenv install --dev
```

Run the migrations to create the database (we use
Postgresql in this case).
```shell
pipenv run ./manage.py migrate
```

The next step is to create an admin account for Django admin.
```shell
pipenv run ./manage.py createsuperuser
```

Finally you can start a development server with:
```shell
pipenv run ./manage.py runserver
```
and see a local version of the website at
[127.0.0.1:8000](http://127.0.0.1:8000/).


### Webpack

Open another terminal and navigate to webpack folder using:
```shell
cd webpack
```

To install webpack dependencies use:
```shell
npm install
```
or alternatively to install from package-lock.json use:
```shell
npm ci
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


### Code Style

After making changes in code and before commit, check code style.
```shell
pipenv run isort .
pipenv run black .
pipenv run flake8 .
```


### Development Blog Posts

[Posts in the Outreachy May 2020 round: CC Legal Database series][blogseries]

[blogseries]: https://opensource.creativecommons.org/blog/entries/legal-database-a-new-beginning/#series


## Guides

The [`guides/`](guides/) folder includes:
- **[`README.md`](guides/README.md)**
- [`deploy_to_heroku.md`](guides/deploy_to_heroku.md)
- [`technologies_used_guide.md`](guides/technologies_used_guide.md)


## License

- [`LICENSE`](LICENSE) (Expat/[MIT][mit] License)

[mit]: http://www.opensource.org/licenses/MIT "The MIT License | Open Source Initiative"
