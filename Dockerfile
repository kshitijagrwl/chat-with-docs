# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-buster as base



# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
ARG UID=10001
RUN apt-get update && apt-get install 

SHELL ["/bin/bash", "-c"]

# Copy the source code into the container.
COPY . .

RUN apt install sqlite3
RUN pip install -r requirements.txt

# Expose the port that the application listens on.
EXPOSE 8000
# Run the application.
CMD uvicorn server:app --host 0.0.0.0 --port 8000