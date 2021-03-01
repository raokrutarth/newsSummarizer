DOCKER_COMPOSE ?= docker-compose
DOCKER_COMPOSE_FILE ?= docker-compose-development.yaml

SERVICES ?= chat scrape cockroachdb
DC_PROJECT ?= local-projectn-prod

start:
	$(DOCKER_COMPOSE) \
		--file $(DOCKER_COMPOSE_FILE) \
		--project-name ${DC_PROJECT} \
		up \
		--detach \
    	--remove-orphans \
    	--force-recreate \
		--build \
		$(SERVICES)

	make -s status

stop:
	$(DOCKER_COMPOSE) \
		--file $(DOCKER_COMPOSE_FILE) \
		--project-name ${DC_PROJECT} \
		down \
		--remove-orphans \
		--volumes
	make -s status

status:
	$(DOCKER_COMPOSE) \
		--file $(DOCKER_COMPOSE_FILE) \
		--project-name ${DC_PROJECT} \
		ps $(SERVICES)

	$(DOCKER_COMPOSE) \
		--file $(DOCKER_COMPOSE_FILE) \
		--project-name ${DC_PROJECT} \
		logs \
		--tail=100

restart:
	make -s stop
	make -s start

logs:
	$(DOCKER_COMPOSE) \
		--file  $(DOCKER_COMPOSE_FILE) \
		--project-name ${DC_PROJECT} \
		logs \
		--tail=100 \
		--follow

deep-clean:
	$(DOCKER_COMPOSE) \
		--file $(DOCKER_COMPOSE_FILE) \
		down \
		--remove-orphans \
		--volumes \
		--rmi all

	docker \
		system prune --volumes --force

