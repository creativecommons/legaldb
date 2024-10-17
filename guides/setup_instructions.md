# Setting Up CreativeCommons/LegalDB

A comprehensive guide for setting up this project on your local machine.

## Prerequisites

Prerequisites for this project are available at [Foundational Technologies - Creative Commons Open Source](https://opensource.creativecommons.org/contributing-code/foundational-tech/).

## Installation Steps

### 1. Fork the Repository

Visit the [creativecommons/Legaldb](https://github.com/creativecommons/legaldb) GitHub page and click the "Fork" button to create your own copy of the repository.

### 2. Clone the Repository

Use any terminal of your choice to run this command

```bash
git clone https://github.com/[your-github-username]/legaldb.git
```
If you are cloning using SSH, the command would look similar to the snippet below

```bash
git clone git@github.com:[your-github-username]/legaldb.git
```

For detailed information on git and cloning, see [Github Docs - Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### 3. Set Up Development Environment

#### Environment Configuration

1. Create a `.env` file:
   - Locate the `.env.template` file in the cloned repository
   - Create a new file named `.env` in the root folder of the repository
   - Copy the contents from `.env.template` to `.env`
   - Configure the following variables:

```env
DJANGO_SECRET_KEY="your_random_string"
DJANGO_DEBUG_ENABLED=True
DJANGO_DATABASE_PASSWORD=postgres  # or your chosen password
DJANGO_SUPERUSER_PASSWORD="your_chosen_password"
DJANGO_TIME_ZONE="UTC"
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_COMPRESS_ENABLED=True
DJANGO_COMPRESS_OFFLINE=True
LIBSASS_OUTPUT_STYLE=
```

#### Start the Development Environment

1. Navigate to the project directory containing the `docker-compose.yml` file
2. Run the Docker Compose command:
```bash
docker compose up
```

> **Note**: Initial setup will take some time as it downloads required containers (~2.6GB for app and ~350MB for db containers)

3. Apply database migrations (in a new terminal):
```bash
docker compose exec app ./manage.py migrate
```

### 4. Accessing the Application

Once everything is set up, access the application at:
```
http://127.0.0.1:8000
```

> **Note**: While the terminal may display `http://0.0.0.0:8000`, use `127.0.0.1:8000` in your browser.

## Troubleshooting

### CRLF Line Ending Issues
If you encounter the following error:
```
/usr/bin/env: 'python3\r': No such file or directory
/usr/bin/env: use -[v]S to pass options in shebang lines
```
This indicates CRLF line ending issues. Solution:
1. Go to the manage.py file in the repo
2. Check the line ending sequence at the bottom left of your code editor (this is the location in vs code) and ensure its LF and not CRLF
3. Do the same thing in step 2 for your `Dockerfile` and your `docker-compose.yml` file
4. Go back to your terminal and run `docker compose build`
5. Finally, run `docker compose up`
6. And your're all set, the application should be running fine now!
