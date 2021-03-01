#!/bin/bash -x

# directory/directories where the auto-linting will be executed
SRC_DIRS=${1:-"app tests"}
echo "Running auto-linting for source code in ${SRC_DIRS}"

isort \
    --force-single-line-imports \
    --use-parentheses \
    ${SRC_DIRS}

autoflake \
    --remove-all-unused-imports \
    --recursive \
    --remove-unused-variables \
    --in-place \
    --exclude=__init__.py \
    ${SRC_DIRS}

black ${SRC_DIRS}
