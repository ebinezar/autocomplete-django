#! /usr/bin/env sh

# run the migration
python manage.py makemigrations books
python manage.py migrate books

# load sample data
python manage.py loaddata --app books books

# Start the server
nginx
exec uwsgi --ini uwsgi.ini
