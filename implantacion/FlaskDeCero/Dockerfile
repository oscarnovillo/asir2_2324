FROM python:3.9.16-alpine3.16

WORKDIR /app

RUN pip3 install gunicorn

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80


ENTRYPOINT [ "/bin/sh", "-c gunicorn --bind 0.0.0.0:80 entry_point:app"]