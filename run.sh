#!/bin/bash

docker run \
    --net=host --rm -it \
    -u 0 \
    -v $PWD/plugins:/home/errbot/plugins \
    -v $PWD/config.py:/home/errbot/config.py \
    -v $PWD/data:/home/errbot/data \
    --entrypoint bash \
    errbotio/errbot:6.1.9
