#!/bin/sh


runDir=$(pwd)
msgGood="\033[32;1m"
msgNeutral="\033[33;1m"
msgBad="\033[31;1m"
msgReset="\033[0m"


runconfigscript(){
    if [ -f "${1}/config.sh" ]; then
        printf "%s" "---"
        printf "${msgGood}Config Script Found At \"${1}\": Running"
        printf "${msgReset}"
        printf "%s\n" "---"
        cd "${1}"
        . ./config.sh
        cd "${runDir}"
    else
        printf "%s" "---"
        printf "${msgNeutral}No Config Script Found At \"${1}\""
        printf "${msgReset}"
        printf "%s\n" "---"
    fi
}

if [ ! -f "./build.lock" ]; then
    touch "./build.lock"
else
    printf "${msgBad}Error: build.lock exists.\nDelete this file to run the build script.\n"
    printf "${msgReset}"

    exit
fi
runconfigscript "./Dockerfiles/liquidSoapDeb"
docker build -t raydio-dev:liquidSoap ./Dockerfiles/liquidSoapDeb
runconfigscript "./Dockerfiles/icecastAlp"
docker build -t raydio-dev:icecast ./Dockerfiles/icecastAlp
