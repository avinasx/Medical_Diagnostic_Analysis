FROM python:3.8.0a3-alpine3.9


ENV PYTHONUNBUFFERED 1



COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


RUN mkdir /project
WORKDIR /project
COPY ./project /project

RUN adduser user
USER user



