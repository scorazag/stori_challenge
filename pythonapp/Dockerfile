FROM python:3.10

RUN pip install mysql-connector-python

WORKDIR /usr/app/src

COPY setup.py database.py logo.jpg mail.py main.py txns.csv ./
