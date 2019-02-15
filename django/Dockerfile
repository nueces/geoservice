FROM python:3
ENV PYTHONUNBUFFERED 1

RUN export DEBIAN_FRONTEND=noninteractive &&\
    apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin libgeos-3.5.1 proj-bin

RUN mkdir /django
COPY . /django
WORKDIR /django

RUN pip3 install --upgrade -r requirements.txt
