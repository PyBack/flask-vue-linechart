FROM python:3.8-slim

WORKDIR /www

ADD . .

RUN python3 -m pip install -U pip
RUN pip3 install -r src/requirements.txt

CMD ["python3",  "src/app.py"]
