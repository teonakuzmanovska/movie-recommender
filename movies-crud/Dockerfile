FROM python:3.10

RUN apt-get -y update; apt-get -y install curl

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]