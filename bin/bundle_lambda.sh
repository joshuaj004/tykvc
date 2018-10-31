#!/bin/bash
#
# creates the zip bundle for AWS lambda
#

set -e

DIR_CUR="$PWD"
ARCHIVE_TMP="/tmp/lambda-bundle-tmp.zip"

addToZip() {
    local exclude_packages="setuptools pip easy_install"
    zip -r9 "$ARCHIVE_TMP" \
        --exclude ./*.pyc \
        --exclude "$exclude_packages" \
        -- "${@}"
}

setUp() {
    if [[ -z $1 ]]; then
        echo "FAIL: missing \$1 argument: output lambda zip filepath"
        exit 1
    fi
    distDir=$(dirname "$1")
    if [[ ! -d "$distDir" ]]; then
        echo "creating dir: $distDir"
        mkdir "$distDir"
    fi
    rm -f "$ARCHIVE_TMP"
    rm -f "$1"
}

addDependenciesToZip() {
    packages_dir=()
    packages_dir+=($(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"))
    env_packages=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(plat_specific=1))")
    if [[ "$env_packages" != "${packages_dir[0]}" ]]; then
        packages_dir+=($env_packages)
    fi

    for (( i=0; i<${#packages_dir[@]}; i++ )); do
        [[ -d "${packages_dir[$i]}" ]] && cd "${packages_dir[$i]}" && addToZip -- *
    done
    cd "$DIR_CUR" || exit 1
}

run() {
    if [[ -z $1 ]]; then
        echo "FAIL: missing \$1 argument: output lambda zip filepath"
        exit 1
    fi
    make deps
    echo "[OK] finished installing dependencies"
    setUp "$1"
    addDependenciesToZip
    addToZip app config ./*.py
    mv "$ARCHIVE_TMP" "$1"
    ls -lh "$1"
}


# shellcheck disable=SC1091
. ./bin/lib/activate-env.sh
sourceEnv

    activatePythonEnv
    run "$1"

if [[ $(uname) == 'Linux' ]]; then
    activatePythonEnv
    run "$1"
else
    echo "[FAIL]: Wrong platform - could not build lambda zip. Must be built on Linux architecture"
    exit 1
fi
