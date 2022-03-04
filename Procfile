# https://devcenter.heroku.com/articles/procfile

# https://devcenter.heroku.com/articles/release-phase
release: ./bin/release_tasks

# https://devcenter.heroku.com/articles/python-gunicorn
web: gunicorn caselaw.wsgi --log-file -
