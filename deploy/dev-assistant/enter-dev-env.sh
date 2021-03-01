#!/bin/bash

# script that sets up aliases and dockerized development tools
# so the development envoirnment is completly host independant (except for Windows OS)

REPO_DIR=${1:-${PWD}}

DC_DIR=${REPO_DIR}/infra

# printf "[+] Local root workspace directory specified in %s: %s\n" ${CONFIG_FILE} ${WS}
echo "[+] Entering dev-assistant with infra directory in ${DC_DIR}"

[ ! -d ${DC_DIR} ] \
    && echo "Directory ${DC_DIR} does not exist. Exiting." \
    && echo "Run `basename $0` from the repository root directory" \
    && exit 1

pushd ${DC_DIR}

# add alias to run the infra assistant in any directory
docker-compose exec \
    --user dev \
    dev-assistant \
    /bin/bash

popd
