#!/bin/sh

start="$(pwd)"
cd "${start}/liquidSoap"
./build.sh
cd "${start}"
cd "${start}/liquidSoapDeb"
./build.sh
cd "${start}"
