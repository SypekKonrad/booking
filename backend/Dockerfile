FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONBUFFERED=1

COPY requirements.txt requirements.txt
RUN apt-get update  && apt-get install -y  postgresql-client gcc
RUN pip install -r requirements.txt
RUN pip install uwsgi


COPY . .

CMD ["uwsgi", "--ini", "uwsgi.ini"]
