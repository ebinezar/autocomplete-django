#! /usr/bin/env sh

nginx
exec uwsgi --ini uwsgi.ini
