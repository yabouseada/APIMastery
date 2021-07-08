FROM debian:buster-slim

RUN apt-get update && apt-get install -y python3.7 python3-pip

ENV APP_ENV=dev
ENV APP_PATH=/var/www/app

WORKDIR ${APP_PATH}

VOLUME ${APP_PATH}

COPY ./entrypoint.sh /tmp/entrypoint.sh

RUN make /tmp/entrypoint.sh

ENTRYPOINT ["/tmp/entrypoint.sh"]