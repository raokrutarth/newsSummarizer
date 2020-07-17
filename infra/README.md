# Deployment Infrastructure

## Overview

Spins up the necessary pods in a given kubernetes container to construct a development/test/production
environment using the values specified in a config file.

## Initiated Services

Creates a namespace in the k8s cluster with:

- Postgres **X5**
- crawl
- chat
- derive
- train
- S3

## Prerequisites

- k8s cluster and it's kubeconfig.
- `yq` (Install with `python -m pip install yq`)
- docker

## Usage

```bash
./start.sh
```

### Development mode

### Test mode

Runs integration tests with mocked responses by each service.

### Production mode

For use in production.
