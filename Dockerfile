FROM python:3

RUN apt-get update

COPY action.py /action.py
COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENTRYPOINT ["python", "/action.py"]


