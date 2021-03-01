#!/bin/bash -ex

# directory/directories where the auto-linting will be executed
SRC_DIRS=${1:-"app tests"}

echo "Running linting checks for source code in ${SRC_DIRS} with directory context $(pwd)"

for src_dir in ${SRC_DIRS}
do
    [ ! -d ./${src_dir} ] \
        && echo "Running lint check with incorrect directory context. Directory ${src_dir} not present" \
        && exit 1
done

poetry run mypy \
    --ignore-missing-imports \
    app

poetry run black \
    --check \
    --diff \
    ${SRC_DIRS}

poetry run isort \
    --check-only \
    --profile black \
    ${SRC_DIRS}

# Use pyline to (only) generate a code similarity report to avoid large amounts
# of code duplication. (NOTE: only running on the app/ source code directory)
poetry run pylint \
    --disable=all \
    --enable=duplicate-code \
    --min-similarity-lines=20 \
    app
