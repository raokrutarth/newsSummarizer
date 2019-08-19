
# doesn't work
# deps:
# 	virtualenv venv
# 	virtualenv -p /Users/krutarthrao/miniconda3/bin/python3.6 venv
# 	source venv/bin/activate


# Makefile allows local package development instead of spawning
# all the other services
clean:
	-docker rm -f chatc dbc

cleani:
	-docker rmi -f chat

img:
	docker build -f $(realpath ./Dockerfile) -t chat:latest .

db:
	docker run \
		--rm \
		--name dbc \
		--env POSTGRES_DB=scratchdb \
		--env POSTGRES_USER=chatApp \
		--env POSTGRES_PASSWORD=myPassword \
		-v $(realpath ../data/postgres):/var/lib/postgresql/data \
		-d \
		postgres:11.4

app:
	docker run \
		--rm \
		--name chatc \
		--link dbc:database \
		-v $(realpath .):/src \
		-it chat:latest bash

run: db app
all: clean img run
