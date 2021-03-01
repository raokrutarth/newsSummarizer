#!/bin/bash

IMG=project-n-dev-assistant

printf "[+] Building and publishing new image %s for dockerized orchestrator env\n" ${IMG}

docker build -t ${IMG} . && \
    printf "[+] Built new image %s\n" ${IMG}
