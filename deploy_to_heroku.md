# Deploy to Heroku


## Process

1. Ensure you have an active and valid Heroku account
2. Install the Heroku CLI
   - See [Getting Started on Heroku with Python | Heroku Dev
     Center][herokupython]
   - Note autocomplete instructions
3. Prepare the app:
   1. Clone the repository using git and change to its directory
   2. Create the app:
        ```shell
        heroku create --team=TEAMNAME
        ```
      - Allow Heroku to set a random name
      - Specify the team (omit if not applicable)
      - If you want a specific Heroku PostgreSQL plan, it's easiest to specify
        it here (ex. `--addons=heroku-postgresql:standard-0`)
3. Mange confign variables (this can be done using the Heroku Dashboard too)
   1. Edit config variables
      - Command
        ```shell
        heroku config:edit
        ```
      - Template (**Be sure to replace the `xxxxxx` values with appropriate
        data**)
        ```
        DJANGO_DEBUG_ENABLED=False
        DJANGO_SECRET_KEY=xxxxxx
        DJANGO_SUPERUSER_EMAIL=xxxxxx
        DJANGO_SUPERUSER_PASSWORD=xxxxxx
        DJANGO_SUPERUSER_USERNAME=admin
        ```
    2. View/verify config variables
        ```shell
        heroku config
        ```
4. Deploy:
    ```shell
    git push heroku main
    ```
   - (If you didn't specify `--addons=heroku-postgresql:xxxxxx`, above, the
     PostgreSQL instance will be created and linked automatically :sparkles:)
5. *(optional)* Change dyno type.
   - :warning: **WARNING: the following command will incur a monthly charge**
    ```shell
    heroku ps:type standard-1x
    ```
6. Open the new app in your browser:
    ```shell
    heroku open
    ```
   - Add `admin/` to the URL to access the admin interface
7. Import database
   - :warning: **WARNING: this assumes any existing data can be destroyed**
    ```shell
    heroku pg:psql < backup.sql
    ```


## Troubleshooting


### Database Backup is in `.dump` format instead of `.sql` format

Convert it:
```shell
pg_restore -f backup.sql backup.dump
```

### psql Connection Error

If you receive an error like the following, ensure a firewall is not blocking
communication on port 5432
```
psql: error: could not connect to server: could not connect to server:
    Connection refused
```


## Documentation

- Heroku Dev Center
  - [Getting Started on Heroku with Python][herokupython]
  - [Configuration and Config Vars][herokuconfig]
  - [Deploying with Git][herokugit]

[herokupython]: https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true
[herokugit]: https://devcenter.heroku.com/articles/git
[herokuconfig]: https://devcenter.heroku.com/articles/config-vars
