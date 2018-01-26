#!/bin/sh

runDir=$(pwd)
printFormatGood="\n---\033[32;1m%s\033[0m---\n"
printFormatNeutral="\n---\033[33;1m%s\033[0m---\n"
printFormatBad="\n---\033[31;1m%s\033[0m---\n"
runconfigscript(){
    if [ -f "${1}/config.sh" ]; then
        printf "${printFormatGood}" "Config Script Found At \"${1}\": Running"
        cd "${1}"
        . ./config.sh
        cd "${runDir}"
    else
        printf "${printFormatNeutral}" "No Config Script Found At \"${1}\""
    fi
}

runconfigscript "./Dockerfiles/liquidSoapDeb"
docker build -t raydio-dev:liquidSoap ./Dockerfiles/liquidSoapDeb
runconfigscript "./Dockerfiles/icecastAlp"
docker build -t raydio-dev:icecast ./Dockerfiles/icecastAlp
