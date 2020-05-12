FROM python:3.8.2-alpine3.11

ENV USERNAME=bcbot
ARG GROUPNAME=bcbot
ARG http_proxy
ARG https_proxy
ARG no_proxy
ARG USERID=1000
ARG GROUPID=1000

RUN apk update\
    && apk upgrade \
    && apk add --no-cache postgresql-dev gcc musl-dev \
    && pip install celery django-celery-beat django_celery_results django-redis psycopg2 \
    && rm -rf /var/cache/apk/* \
    && adduser --disabled-password -u ${USERID} -g ${GROUPID} ${USERNAME} ${GROUPNAME}

WORKDIR /home/${USERNAME}/${USERNAME}

COPY docker-entrypoint1.sh /opt

user ${USERNAME}

#ENTRYPOINT ["/opt/docker-entrypoint1.sh"]
