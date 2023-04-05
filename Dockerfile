FROM python:3.11.2-slim-buster
COPY ./app/requirements.txt /
RUN pip install -r requirements.txt
