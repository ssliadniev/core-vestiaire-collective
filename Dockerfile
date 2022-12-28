FROM python:3.9-buster as base
LABEL maintainer.contact="s.sliadniev@quantumobile.com"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH=$PYTHONPATH:/usr/src/app
RUN pip install -U pip
COPY requirements/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
CMD bash