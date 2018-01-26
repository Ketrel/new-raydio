#!/bin/sh
if [ "${1}" = "int" ]; then
    docker run -it --rm raydio-dev:icecast /bin/sh
else
    docker run --rm -d raydio-dev:icecast /bin/sh
fi
