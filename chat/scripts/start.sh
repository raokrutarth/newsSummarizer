#!/bin/bash -ex

# Start the application

PORT=${1:-"4000"}

# set pythonpath
export PYTHONPATH=${PYTHONPATH}:"$(pwd)/app"

# activate python venv
source "$(poetry env info --path)/bin/activate"

if [[ -v RUN_GUNICORN ]]; then
    # mostly for production
    gunicorn \
        --bind=0.0.0.0:"${PORT}" \
        --workers 2 \
        --worker-class uvicorn.workers.UvicornWorker \
        --log-level ${LOGLEVEL:-"info"} \
        main:app
else
    # TODO move to dynaconf based runtime setting
    export RUNTIME_MODE="development"

    uvicorn \
        --host 0.0.0.0 \
        --port ${PORT} \
        --reload \
        --log-level ${LOGLEVEL:-"info"} \
        --use-colors \
        main:app
fi

