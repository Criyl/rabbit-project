from python:3.8


RUN apt-get update && apt-get upgrade && apt-get install -y supervisor

WORKDIR /app

RUN python -m venv .venv &&\
    echo .venv/ >> .gitignore 

COPY requirements.txt .
RUN . .venv/bin/activate &&\
    echo Celery >> requirements.txt &&\
    python -m pip install -r requirements.txt

COPY . .
ENTRYPOINT . .venv/bin/activate && celery -A rabbit_project worker -Q special,default -l info