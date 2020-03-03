FROM ubuntu:18.04
LABEL maintainer="Chris Buckner<christopher.d.buckner@gmail.com>"

EXPOSE 80

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# required for fastapi to run
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	libev-dev \
	net-tools \
	telnet \
	curl \
	vim

RUN pip3 install \
	fastapi[all] \
	gunicorn \
	uvicorn \
	jinja2 \
	aiofiles
	
# Add demo app
COPY web-app/Dog/ /Dog
WORKDIR /Dog
CMD uvicorn app:app --host 0.0.0.0 --port 80
