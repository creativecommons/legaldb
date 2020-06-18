# See https://devcenter.heroku.com/articles/release-phase
release: python manage.py migrate && python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() or User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')"

# See https://devcenter.heroku.com/articles/python-gunicorn
web: gunicorn caselaw.wsgi --log-file -
