FROM python:3.7

#Run python in unbuffered mode to allow for log messages to be
#immediately dumped to the stream instead of being buffered.
ENV PYTHONUNBUFFERED 1

RUN apt-get update

# Copying app to docker and making it as working directory
RUN mkdir /app
WORKDIR /app
COPY ./ /app

# Install all dependencies
RUN pip install pipenv
RUN pipenv install --system

#Creating a user
RUN useradd -ms /bin/bash user
USER user