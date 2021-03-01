#!/bin/bash -ex

source "$(poetry env info --path)/bin/activate"


SRC_DIRS="./app ./tests"

autoflake \
    --remove-all-unused-imports \
    --recursive \
    --remove-unused-variables \
    --in-place \
    --exclude=__init__.py \
    ${SRC_DIRS}

isort \
    --multi-line=3 \
    --trailing-comma \
    --force-grid-wrap=0 \
    --combine-as \
    --line-width 88 \
    ${SRC_DIRS}

black ${SRC_DIRS}

mypy \
    --ignore-missing-imports \
    ${SRC_DIRS}