#!/bin/bash -ex

# Start a local instance of the application for development
source "$(poetry env info --path)/bin/activate"

PORT=${1:-"4001"}

# set pythonpath
export PYTHONPATH="$(pwd)/app":${PYTHONPATH}

# set runtime with env var
export SCRAPECONF_RUNTIME_MODE="development"

if [[ -v RUN_GUNICORN ]]; then
    gunicorn \
        --bind=0.0.0.0:"${PORT}" \
        --workers 2 \
        --worker-class uvicorn.workers.UvicornWorker \
        --log-level ${LOGLEVEL:-"info"} \
        main:app
else
    uvicorn \
        --host 0.0.0.0 \
        --port ${PORT} \
        --reload \
        --log-level ${LOGLEVEL:-"info"} \
        --use-colors \
        main:app
fi

