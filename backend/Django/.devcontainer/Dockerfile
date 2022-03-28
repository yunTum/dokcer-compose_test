FROM python:3.8
LABEL architecture="Aonuma" 

ENV PYTHONUNBUFFERED true

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt /app/

RUN pip3 install -r requirements.txt

