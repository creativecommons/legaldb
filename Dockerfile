# https://docs.docker.com/engine/reference/builder/

# https://hub.docker.com/_/python/
# https://devcenter.heroku.com/articles/python-support
# Match version to Heroku app
# Keep in sync with .github/workflows/main.yml and Pipfile
FROM python:3.12

# Configure apt not to prompt during docker build
ARG DEBIAN_FRONTEND=noninteractive

# Python: disable bytecode (.pyc) files
# https://docs.python.org/3.9/using/cmdline.html
ENV PYTHONDONTWRITEBYTECODE=1

# Python: force the stdout and stderr streams to be unbuffered
# https://docs.python.org/3.9/using/cmdline.html
ENV PYTHONUNBUFFERED=1

# Python: enable faulthandler to dump Python traceback on catastrophic cases
# https://docs.python.org/3.9/library/faulthandler.html
ENV PYTHONFAULTHANDLER=1

WORKDIR /root

# Configure apt to avoid installing recommended and suggested packages
RUN apt-config dump \
| grep -E '^APT::Install-(Recommends|Suggests)' \
| sed -e's/1/0/' \
| tee /etc/apt/apt.conf.d/99no-recommends-no-suggests

# Resynchronize apt package index
RUN apt-get update

# Install apt package dependencies
RUN apt-get install -y g++ gcc gettext postgresql-server-dev-all

## Install pipenv
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade pipenv

# Install python dependencies
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv sync --dev --system

# Create mount point for docker-compose volume and set as current workdir
WORKDIR /legaldb

# Create non-root user
RUN useradd --create-home --shell /bin/bash user
USER user
