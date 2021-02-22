FROM python:3.7

#Run python in unbuffered mode to allow for log messages to be
#immediately dumped to the stream instead of being buffered.
ENV PYTHONUNBUFFERED 1

RUN apt-get update

# Copying app to docker and making it as working directory
RUN mkdir /legaldb
WORKDIR /legaldb

# Install Python dependency management tools
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install --upgrade pipenv

# Copy the Pipenv files into the container
COPY Pipfile /legaldb/
COPY Pipfile.lock /legaldb/

# Install the dependencies system-wide
RUN pipenv install --deploy --system --dev

#Creating a user
RUN useradd -ms /bin/bash user
USER user
