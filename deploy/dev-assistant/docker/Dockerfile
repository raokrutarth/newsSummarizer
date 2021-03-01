FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true
ENV container docker

RUN apt update && apt-get install --yes --no-install-recommends \
    build-essential \
    software-properties-common \
    gpg-agent \
    init \
    systemd-container \
    net-tools\
    sudo \
    curl \
    ca-certificates \
    locales \
    openssh-client \
    iputils-ping \
    apt-transport-https \
    gnupg-agent \
    inotify-tools

# Set the locale
ENV LANG en_US.UTF-8
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8

# Installing dev tools
RUN apt update && apt-get install --yes --no-install-recommends \
    vim \
    zip \
    tree \
    groff \
    bash-completion \
    less \
    git \
    jq \
    netcat \
    sed

RUN add-apt-repository -y ppa:deadsnakes/ppa && \
    apt install --yes --no-install-recommends \
    isort \
    python3.7 \
    python3.7-dev \
    python3.7-venv && \
    ln -s /usr/bin/python3.7 /usr/local/bin/python

RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py \
    && python3.7 /tmp/get-pip.py pip \
    && rm /tmp/get-pip.py

# TODO install Golang toolkit

# Install SSH Server
RUN apt update && apt-get --yes --no-install-recommends install \
    openssh-server && \
    mkdir -p /var/run/sshd && \
    chmod 0755 /var/run/sshd && \
    echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
    sed -i 's/AcceptEnv/# AcceptEnv/' /etc/ssh/sshd_config

# install kubectl
RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl

# TODO Installing Helm

# TODO Installing Stern

# TODO Installing Skaffold

# Installing docker
RUN echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
    && apt update \
    && apt-get --yes --no-install-recommends install docker.io

# Creating the dev user
RUN useradd --create-home -s /bin/bash dev && \
    usermod -a -G docker dev && \
    ln -s /home/dev/.profile /home/dev/.bash_profile && \
    mkdir -p /home/dev/.ssh && \
    echo -n 'dev:dev' | chpasswd && \
    echo 'dev ALL=NOPASSWD: ALL' > /etc/sudoers.d/dev && \
    mkdir -p /home/dev/.ssh /workspace && \
    chown -R dev:dev /home/dev /workspace /var/run

COPY ./bashrc /tmp/bashrc
RUN cat /tmp/bashrc >> /home/dev/.bashrc && rm /tmp/bashrc

# Installing awscli
RUN pip3.7 install awscli-local>=0.6

# TODO Installing psql

# Installing redis-cli
RUN apt update && \
    apt install --yes --no-install-recommends redis-tools

# Installing environment variables file for localstack
ENV LOCALSTACK_HOST localstack
RUN echo "export LOCALSTACK_HOST=${LOCALSTACK_HOST}" >> /etc/profile.d/localstack.sh

# Don't start any optional services except for the few we need.
RUN find /etc/systemd/system \
    /lib/systemd/system \
    -path '*.wants/*' \
    -not -name '*journald*' \
    -not -name '*systemd-tmpfiles*' \
    -not -name '*systemd-user-sessions*' \
    -not -name '*ssh*' \
    -not -name '*docker*' \
    -not -name '*binfmt*' \
    -exec rm \{} \;
RUN systemctl set-default multi-user.target

# Install poetry
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    # paths
    # this is where the requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
    && chown dev:dev -R /opt

ENV PATH=/opt/poetry/bin:$PATH

WORKDIR /workspace

CMD ["/sbin/init"]
