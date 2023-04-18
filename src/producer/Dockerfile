FROM python:3.8-slim-buster

ARG host="localhost:29092"
ARG topic="topic"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY producer.py producer.py
COPY archive/. archive/.

CMD "python3" "producer.py" "${host}" "${topic}"