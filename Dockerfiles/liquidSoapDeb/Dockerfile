FROM debian:stretch-slim

RUN apt-get update && \
    apt-get -yqq install liquidsoap python3

COPY ./files/launcher.py /launcher.py
