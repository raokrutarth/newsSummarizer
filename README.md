# newsSummarizer

Answers direct questions from selected sources through a chatbot.

## Design

[Design Doc](https://docs.google.com/document/d/1VSOjpRiMYwyWRsGnEiJc1dSoIOWX7MYKEzPeqAmE9c8/edit#)

## Usage

- Local development ports:
  - chat: 4000
  - scrape: 4001
  - learn: 4002
  - archive: 4003

## Progress

- Infra and derive docker-compose working.
- cockroach DB init script completed.
  - may have timing issues with db creation and clients startup.

- TODO
  - Use one of below for config parsing.
    - <https://github.com/rochacbruno/dynaconf>
    - <https://github.com/rednafi/konfik>
  - Use <https://github.com/sourcery-ai/python-best-practices-cookiecutter/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/.github/workflows/test.yml> for all python best practices automation.
  - Use learn to bring up example model on REST API.
  - Use HAProxy and connect it with development workflows.
    - <https://blog.hypriot.com/post/docker-compose-nodejs-haproxy/>
    - <https://github.com/GagePielsticker/Express-API-Boilerplate/blob/master/docker-compose.yml>
  - Or traefik:
    - <https://github.com/fabioassuncao/docker-boilerplate-traefik-proxy/blob/master/docker-compose.yml>
    - <https://github.com/JeffersonBC/docker-boilerplates/blob/master/traefik/traefik.toml>
    - Traefik, hydra, jaeger and monitoring containers: <https://github.com/derekbar90/catalyst>
  - Use Oauth 2.0 server: <https://github.com/ory/hydra>
  - Swap out model with NLP library model.
  - Add other NLP library models.
  - Add spark and elastic search to envoirnment.
  - Deploy DB and derive and make sure the logs show successful sql alchemy connection.
  - test derive endpoints with manual REST calls and browser access. Verify data is inserted and fetched from DB.
  - Write setting and config management module for derive.
  - Connect derive to s3 and verify data fetching and pushing works correctly.
  - Add in-app metrics to derive. (Resist urge to add prometheus. backlog it.)
  - Change DB ORM to reflect user and articles table.
  - Replicate build infra for other micro-services and verify DB connection is successful.
  - Begin working on chat by migrating existing code to new infra.

### Development decisions

- Decision
  - Moving development env to docker-compose instead of k8s+skaffold+minikube.
  - Will use skaffold to deploy to k8s when needed (be mindful of custom scripts).
    - Should not be needed until a multi-machine execution envoirnment is needed
      due to fail-over and load balancing needs.
  - Reasons:
    - Difficult to do development with minikube with a container based dev-env.
    - Skaffold needs to be pointed to modified kubeconfig and docker daemon.
    - minikube cert file paths in the kubeconfig need to be mounted and updated.
    - docker image pull credentials need to be sent to the minikube cluster & in k8s artifacts.
  - Use [poetry environments](https://python-poetry.org/docs/managing-environments/) instead of a development container.
    - Development container is difficult to configure and manage with littl upside over single machine for now.
    - `sudo apt-get install python3.7-venv`
    - `poetry config virtualenvs.create true`
    - `poetry env list`
    - `poetry config --list`
    - `poetry env use python3.7`
