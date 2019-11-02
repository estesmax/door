FROM python:3.8

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . /usr/src/app

CMD python3 door.py
