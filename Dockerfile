FROM python:3.8.6-buster

RUN mkdir -p /opt/sampleFlask/app

COPY app/ /opt/sampleFlask/app/
COPY requirements.txt /opt/sampleFlask/requirements.txt

WORKDIR /opt/sampleFlask/app/

RUN pip install -r /opt/sampleFlask/requirements.txt

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]