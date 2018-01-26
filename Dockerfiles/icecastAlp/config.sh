#!/bin/sh
. ./config.opt
sed \
    -e 's/{{ location }}/'"${location}"'/' \
    -e 's/{{ adminEmail }}/'"${adminEmail}"'/' \
    -e 's/{{ maxSources }}/'"${maxSources}"'/' \
    -e 's/{{ sourcePassword }}/'"${sourcePassword}"'/' \
    -e 's/{{ listenPort }}/'"${listenPort}"'/' \
    -e 's/{{ relayPassword }}/'"${relayPassword}"'/' \
    -e 's/{{ adminUser }}/'"${adminUser}"'/' \
    -e 's/{{ adminPassword }}/'"${adminPassword}"'/' \
    ./files/templates/icecast.xml.tpl > ./files/staging/icecast.xml

#rm ./staging/icecast.xml
