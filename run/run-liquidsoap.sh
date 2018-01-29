#!/bin/sh
if [ "${1}" = "int" ]; then
    docker run -it --rm -p 8887:8887 raydio-dev:liquidSoap /bin/bash
else
#    docker run --rm -d -p 8887:8887 raydio-dev:liquidSoap /usr/bin/python3 /launcher.py
    docker run --rm -d -p 8887:8887 raydio-dev:liquidSoap /start.sh
fi
