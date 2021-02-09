FROM python:3.8
COPY ./company /
COPY ./requirements.txt /company
WORKDIR /company
RUN pip install -r requirements.txt