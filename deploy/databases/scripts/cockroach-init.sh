#/bin/bash

#########################
# Script to be run in the same context as the docker compose file to create the necessary databases
# and users after the container is up.
# NOTE
#   Moving to k8s deployment will mean the EXEC_CMD will change to a kubectl command possibly.
#########################

DC_SERVICE_NAME="cockroachdb"
EXEC_CMD="docker-compose exec -u root ${DC_SERVICE_NAME} cockroach sql --insecure --execute="

# Use a default password for acc databases if one is not provided
# TODO passwords only work in secure mode. Secure mode requires certs
# DB_PASSWORD=${DB_PASSWORD-mysecret}

# create the databases and assign users
DB_NAMES=("derive" "chat" "learn" "scrape" "archive")
printf "Initalizing cockroachdb with databases %s.\n" "${DB_NAMES}"

for db_name in $DB_NAMES;
do
	printf "Creating database %s\n" ${db_name}
	${EXEC_CMD}"CREATE DATABASE ${db_name};"

	DATABASE_USER=${db_name}
	# echo "Creating DATABASE_USER [${DATABASE_USER}] with DATABASE_PASSWORD [${DB_PASSWORD}]"
	# ${EXEC_CMD}"CREATE USER ${DATABASE_USER} WITH PASSWORD '${DB_PASSWORD}';"

	echo "Creating database user [${DATABASE_USER}]"
	${EXEC_CMD}"CREATE USER ${DATABASE_USER};"
	${EXEC_CMD}"GRANT ALL ON DATABASE ${db_name} TO ${DATABASE_USER};"
	${EXEC_CMD}"GRANT admin TO ${DATABASE_USER};"
done
