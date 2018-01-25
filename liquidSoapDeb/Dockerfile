FROM debian:stretch-slim

RUN apt-get update && \
    apt-get -yqq install liquidsoap python3

COPY ../python/launcher.py /launcher.py
