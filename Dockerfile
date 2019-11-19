 FROM python:3.7.5-buster 

RUN apt-get update

COPY . /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt