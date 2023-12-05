# syntax=docker/dockerfile:1.4

ARG ERRBOT_VERSION=6.1.9

FROM scratch AS dependencies
COPY requirements.txt /app/

FROM errbotio/errbot:${ERRBOT_VERSION}
ARG ERRBOT_SLACKV3_VERSION=0.2.1

USER root
RUN --mount=type=bind,from=dependencies,source=/app,target=/app,rw \
    git clone -b v${ERRBOT_SLACKV3_VERSION} \
      https://github.com/errbotio/err-backend-slackv3 \
      /usr/local/lib/python3.9/site-packages/errbot/backends/slackv3 && \
    pip3 install --no-cache errbot-backend-slackv3==${ERRBOT_SLACKV3_VERSION} && \
    pip3 install --no-cache -r /app/requirements.txt

USER errbot
STOPSIGNAL SIGINT
