FROM python:3.9.0

ENV PYTHONUNBUFFERED true

RUN mkdir -p /backend
WORKDIR /backend

ADD requirements.txt /backend/

RUN pip3 install -r requirements.txt

