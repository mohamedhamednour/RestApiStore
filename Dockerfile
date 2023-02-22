FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt




