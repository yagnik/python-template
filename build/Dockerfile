FROM python:3
WORKDIR /opt/project

ENV PIPENV_SHELL bash

COPY Pipfile* /opt/project/
COPY build/py.sh /usr/local/bin/py.sh

RUN pip install pipenv && pipenv install --dev
