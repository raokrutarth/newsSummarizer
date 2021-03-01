#!/bin/bash -x

# script to run unit tests. Run when in learn/ so relative paths
# dont cause issues
# -----
# Run with: poetry run ./scripts/run-tests.sh

# TODO hacky way to make sure the import paths in the
# app/ dir are not prefixed by app.
export PYTHONPATH=$(realpath ./app):${PYTHONPATH}

TESTS=${1:-"test"}

# run tests with coverage, listing test time,
pytest \
    --cov=app \
    --new-first  \
    --durations=0 \
    --showlocals \
    --log-level=${LOGLEVEL:-DEBUG} \
    --log-cli-level=${LOGLEVEL:-WARN} \
    --log-file=${LOGFILE:-test_results.log} \
    -k ${TESTS} \
    ./tests

echo "Tests complete. Application logs in ${LOGFILE:-test_results.log}"
