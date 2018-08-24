FROM python:3.6

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./api.ini /api.ini

CMD ["/usr/local/bin/uwsgi", "--ini", "/api.ini"]

