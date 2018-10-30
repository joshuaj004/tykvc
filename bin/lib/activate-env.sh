#!/usr/bin/env bash

sourceEnv() {
    if [[ -f .env ]]; then
        # shellcheck disable=SC1091
        . .env
    fi
}

activatePythonEnv() {
    if [[ ! -d env ]]; then
        make env
    fi

    if [[ $VIRTUAL_ENV != $PWD/env ]]; then
        # shellcheck disable=SC1091
        . env/bin/activate
    fi
}
