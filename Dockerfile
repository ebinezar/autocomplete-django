FROM python:3.8-alpine3.12

# Intall requirements
RUN apk update
RUN apk add --update \
  build-base \
  mariadb-dev \
  mysql-client \
  linux-headers \
  nginx \
  nginx-mod-http-headers-more \
  && rm -rf /var/cache/apk/*

# Create required directories
RUN mkdir -p /var/app
RUN mkdir -p /var/log/uwsgi
RUN mkdir -p /var/run/uwsgi

#Ngnix
COPY nginx.conf /etc/nginx
RUN ln -sf /dev/stdout /var/log/nginx/access.log

# Copy application code
COPY . /var/app

# Change to the application's directory
WORKDIR /var/app

# Install python libs
RUN pip install setuptools --upgrade
RUN pip install -r /var/app/requirements.txt --no-cache-dir

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/bin/sh" ]
CMD [ "entrypoint.sh" ]
