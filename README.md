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


#### Initialize database with development data

The following utility will reset the database, run migrations, configure an
admin user, and load the developiment data:
1. In a terminal window / command line:
    ```shell
    docker compose up
    ```
2. In a second terminal window /command line:
    ```shell
    ./bin/init_data.sh
    ```

#### Helper commands

All of the following helper commands assume the App and DB services are
running:
- [`bin/check.sh`](bin/check.sh)
  - _Perform static analysis checks and reformat Python code_
- ~~[`bin/dump_data.sh`](bin/check.sh)~~
  - ~~_Dump Django data with processing to remove PII and unapproved
    entries_~~
  - Not normally invoked during development
- [`bin/init_data.sh`](bin/init_data.sh)
  - _Initialize Django application data (!!DANGER!!)_
- ~~[`process_data.py`](bin/process_data.py)~~
  - ~~_Process YAML data from Django dumpdata to remove PII and unapproved
    entries._~~
  - ~~called by `bin/dump_data`~~
  - Not normally invoked during development
- ~~[`bin/release_tasks`](bin/release_tasks)~~
  - ~~Heroku release script~~
  - Not normally invoked during development
- [`bin/test.sh`](bin/check.sh)
  - _Run Django collectstatic, check, and test (unit tests)_


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
  - (better to use `bin/init_data.sh`)
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
  - (better to use `bin/test.sh`)


### Pipenv

The Python modules are managed by [Pipenv](https://pipenv.pypa.io/en/latest/).
If development requires new Python modules, remember to also rebuild your
Docker containters.


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

After making changes in code and before commit, check code style:
```shell
./bin/check.sh
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
