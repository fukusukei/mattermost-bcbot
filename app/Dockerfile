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
    && apk --no-cache add tzdata \
    && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && pip install requests \
    && rm -rf /var/cache/apk/* \
    && adduser --disabled-password -u ${USERID} -g ${GROUPID} ${USERNAME} ${GROUPNAME} 

WORKDIR /home/${USERNAME}

user ${USERNAME}
