# syntax=docker/dockerfile:1
FROM ubuntu:20.04
FROM python:3.9.5
LABEL Author="PaninStanislav"

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl

RUN pip install --upgrade pip
COPY ./requirements.txt /project/
RUN pip install -r requirements.txt

COPY . /project/
EXPOSE 8000