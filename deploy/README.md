# Deployment Infrastructure

## Overview

Spins up the necessary pods in a given kubernetes container to construct a development/test/production
environment using the values specified in a config file.

## Initiated Services

Creates a namespace in the k8s cluster with:

- Cockroachdb/Postgres
- scrape
- chat
- derive
- learn
- S3

## Prerequisites

- Docker
- k8s cluster and it's kubeconfig.

  **Minikube**

  ```bash
  # follow instructions on https://kubernetes.io/docs/tasks/tools/install-minikube/
  # For ubuntu, install virtualbox too: https://phoenixnap.com/kb/install-minikube-on-ubuntu
  # setting up host docker and minikube for local images: https://magda.io/docs/installing-minikube.html
  minikube config set memory 8192
  minikube config set cpus 4
  minikube config set vm-driver virtualbox
  minikube start
  ```

- `yq`

  ```bash
  python -m pip install yq
  ```

## Usage

- `cp config-template.yaml config.yaml`
- Fill out `config.yaml` as described by comments in file.
- Start & enter `dev-assistant` container with command.

  ```bash
  ./start.sh
  ```

- Use `start-cluster` to enter one of the modes described below.

  ```bash
  root@/workspace$ start-cluster
  ```

  __NOTE__ `start-cluster` reads the values from `config.yaml` to setup the cluster as specified in the config file.

### Development mode

- Start cockroachdb cluster on local k8s with **NO** mounted volume.
  - generate certs, creds & connection configs.
  - store certs, creds and connection strings in accessible location (file/env var/k8s config map/k8s secrets)
  - verify the DB is up and running.
- Modify and deploy each microservice to cluster with [skaffold dev](https://www.youtube.com/watch?v=tTNrzEjROCo). For example:

  ```bash
  cd /ws/derive
  skaffold dev
  ```

#### During Development

- Sksffold should already tail logs and auto-update pods as source code is modified.
- Run unit tests in a given microservice's directory. For example:

  ```bash
  cd /ws/derive/tests
  run_ut.sh
  ```

### Test mode - TODO

Runs feature and integration tests with mocked responses by each service.

### Production mode - TODO

For use in production.
