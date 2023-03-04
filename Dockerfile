FROM python:3.11
ENV PYTHONBUFFERED 1

COPY . /app
WORKDIR /app
RUN pip3 install -r req.txt


