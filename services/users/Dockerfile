FROM python:3.11.4-slim-bullseye as python

ARG BUILD_ENVIRONMENT=local

# Python build stage
FROM python as python-build-stage

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

COPY ./services/users/requirements.txt .

RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r requirements.txt


WORKDIR /users