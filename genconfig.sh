#!/bin/sh

gen(){
    printf "%s\n" $(cat /dev/urandom | \
                    tr -dc 'a-zA-Z0-9!@#$%^&*' | \
                    fold -w 256 | \
                    sed -e 's/[oO]/0/g' | \
                    head --bytes 32)
}

echo "Example: $(gen)"
