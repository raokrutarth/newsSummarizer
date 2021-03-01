#!/bin/bash -ex

docker build --tag scrape:"$(git rev-parse HEAD)" .