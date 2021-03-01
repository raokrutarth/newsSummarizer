
##### Stage 1 #####
FROM python:3.7 AS builder

ENV APP_ROOT_DIR="/opt/derive"
RUN mkdir -p $APP_ROOT_DIR
WORKDIR $APP_ROOT_DIR

# poetry env vars
ENV POETRY_NO_INTERACTION=1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_VERSION=1.0.10

# Update path with poetry executables
ENV PATH="$POETRY_HOME/bin:${APP_ROOT_DIR}/.venv/bin:$PATH"

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python


# install deps in specific folder so they can be copied
COPY ./pyproject.toml ./poetry.lock* ${APP_ROOT_DIR}/
RUN poetry install


############### Stage 2  ####################
FROM builder as development

WORKDIR $APP_ROOT_DIR

COPY --from=builder $POETRY_HOME $POETRY_HOME
COPY --from=builder ${APP_ROOT_DIR}/.venv ${APP_ROOT_DIR}/.venv

COPY ./app/* ${APP_ROOT_DIR}/

ENV PYTHONPATH=$PYTHONPATH:${APP_ROOT_DIR}

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]
