#!/bin/bash -x

# script to run unit tests. Run when in learn/ so relative paths
# dont cause issues
# -----
# Run with: poetry run ./scripts/run-tests.sh

# selective test name. Only run tests containing this substring
# in the test name. defaults to all tests.
TESTS=${1}

# FIXME hacky way to make sure the import paths in the
# app/ dir are not prefixed by app.
export PYTHONPATH=$(realpath ./app):${PYTHONPATH}

# run tests with coverage, listing test time,
pytest \
    --cov=app \
    --cov-report=term-missing \
    --cov-fail-under 70 \
    --failed-first  \
    --exitfirst \
    --durations=0 \
    --log-level=${LOGLEVEL:-DEBUG} \
    --log-cli-level=${LOGLEVEL:-WARN} \
    --log-file=${LOGFILE:-test_results.log} \
    -k ${TESTS:-.} \
    tests
