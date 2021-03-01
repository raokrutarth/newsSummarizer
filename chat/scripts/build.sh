#!/bin/bash -ex

docker build --tag chat:"$(git rev-parse HEAD)" .