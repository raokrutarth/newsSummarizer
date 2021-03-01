##### Stage 1 #####
FROM python:3.8 AS builder

ENV APP_ROOT_DIR="/opt/scrape"
RUN mkdir -p $APP_ROOT_DIR
WORKDIR $APP_ROOT_DIR

# poetry env vars
ENV POETRY_NO_INTERACTION=1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Update path with poetry executables
ENV PATH "${POETRY_HOME}/bin:${APP_ROOT_DIR}/.venv/bin:${PATH}"

# install deps in specific folder so they can be copied
COPY ./pyproject.toml ./poetry.lock ${APP_ROOT_DIR}/
RUN poetry install --no-dev

############### Stage 2  ####################
FROM builder as execution

WORKDIR ${APP_ROOT_DIR}

COPY --from=builder ${POETRY_HOME} ${POETRY_HOME}
COPY --from=builder ${APP_ROOT_DIR}/.venv ${APP_ROOT_DIR}/.venv

ENV SCRAPECONF_RUNTIME_MODE "production"

COPY ./app ./app
COPY ./scripts/start.sh ./start.sh

ENV PYTHONPATH="${PYTHONPATH}:${APP_ROOT_DIR}/app"
RUN poetry shell
ENTRYPOINT ["/opt/scrape/start.sh"]
