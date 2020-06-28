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

RUN mkdir -p /var/app
RUN mkdir -p /var/log/uwsgi
RUN mkdir -p /var/run/uwsgi

ADD requirements.txt /var/app
RUN pip install setuptools --upgrade
RUN pip install -r /var/app/requirements.txt --no-cache-dir

#Ngnix
COPY nginx.conf /etc/nginx

#Logrotate config
RUN mkdir -p /log/old/uwsgi

#Start All process
COPY start.sh /start.sh
COPY uwsgi.ini /uwsgi.ini
RUN chmod +x /start.sh
COPY . /var/app
RUN ln -sf /dev/stdout /var/log/nginx/access.log

ENTRYPOINT [ "/bin/sh" ]
CMD [ "/start.sh" ]
