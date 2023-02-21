FROM python:alpine3.9
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN apt install apturl
RUN apt install Brlapi
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000", "--settings=app.settings.prod" ]



