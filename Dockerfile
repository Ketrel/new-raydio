FROM alpine:3.6

RUN touch ~/.profile && \
    apk add --no-cache m4 pcre-dev gcc g++ libc-dev make opam patch python3 && \
    apk add --no-cache lame lame-dev libogg libogg-dev libvorbis libvorbis-dev libmad libmad-dev libsamplerate libsamplerate-dev taglib taglib-dev && \
    opam init -a && \
    eval $(opam config env) && \
    #
    unlink /usr/bin/whoami && \
    printf "#!/bin/sh\nprintf \"notroot\\n\"">/usr/bin/whoami && \
    chmod +x /usr/bin/whoami && \
    #
    opam install -y conf-m4 && \
    opam install -y taglib mad lame vorbis cry samplerate liquidsoap && \
    #
    rm /usr/bin/whoami && \
    ln -s /bin/busybox /usr/bin/whoami

COPY ./python/launcher.py /launcher.py
