# legaldb

<p align="center">
    <a href="https://github.com/creativecommons/caselaw/blob/master/LICENSE"><img alt="MIT license" src="https://img.shields.io/github/license/creativecommons/vocabulary.svg?color=brightgreen"/></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

CC Legal Database: curated repository of Case Law and Scholarship data from
around the world in a Django based website.

**[legaldb.creativecommons.org](https://legaldb.creativecommons.org/)**


## Code of Conduct

Please note that this project is released with a Contributor [Code of
Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to
abide by its terms.


## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). It contains some general instructions
that should be followed when contributing to any of the Creative Commons
open-source repositories.


## Development setup

Copy `.env.template` and set environment variables (like
`DJANGO_DEBUG_ENABLED=True` for local development and testing) and secret keys
in a `.env` file.
```shell
cp .env.template .env
```


### Using docker compose

Ensure that you have Docker and Docker Compose installed on your system
For installation instructions refer: [Get Docker | Docker
Documentation](https://docs.docker.com/get-docker/)


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

### Cloning Code Into Your CodeEditor

1. Open https://github.com/creativecommons/legaldb in your browser, it will redirect you to the github repository of Creative Common's legaldb.

2. Here you will see all the folders and files present in the repository, somewhat at the middle-right of the screen you will find a green button saying "Code" with a arrow within it.

3. Tap on the arrow and you have three options before you, first will be HTTPS, second will be SSH and third will be GitHub CLI.

4. By default you will be on the first option HTTPS and that is what we will use to clone the code.

5. In this option (First one HTTPS) you will see a URL or Link in a box below which "Clone using the web URL" will be written, simply copy the URL or Link.

6. Now open the code editor you use (Visual Studio Code recommended and used here), then open the folder you want to clone the code in.

7. Then open bash terminal within your code editor and type the following git command:

```shell 
git clone https://github.com/creativecommons/legaldb.git
```

8. Here in this command I have already pasted the URL or Link you have copied from github.

9. Press Enter after typing this command and the code will be cloned in your code editor and you are free to edit it.

10. Recommended: Use of Visual Studio Code and knowledge of Git and GitHub and some terminal commands. (Can watch some videos on Youtube to know about Git and GitHub)



### Development Blog Posts

[Posts in the Outreachy May 2020 round: CC Legal Database series][blogseries]

[blogseries]: https://opensource.creativecommons.org/blog/entries/legal-database-a-new-beginning/#series


## Deploy to Heroku

See [`deploy_to_heroku.md`](deploy_to_heroku.md).


## License

- [`LICENSE`](LICENSE) (Expat/[MIT][mit] License)

[mit]: http://www.opensource.org/licenses/MIT "The MIT License | Open Source Initiative"
