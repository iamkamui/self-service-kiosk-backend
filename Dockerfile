FROM python:3.12.2-alpine3.19
WORKDIR /code
RUN apt-get update && apt-get upgrade
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
