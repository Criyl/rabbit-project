from python:3.8


WORKDIR /app

RUN python -m venv .venv &&\
    echo .venv/ >> .gitignore 

COPY requirements.txt .
RUN . .venv/bin/activate &&\
    echo gunicorn >> requirements.txt &&\
    python -m pip install -r requirements.txt

COPY . .
ENTRYPOINT . .venv/bin/activate && python manage.py migrate && python manage.py runserver 0.0.0.0:8000