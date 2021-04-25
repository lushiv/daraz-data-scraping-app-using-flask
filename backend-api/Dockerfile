FROM python:3.7

WORKDIR /flask-app-base

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./flask-app ./flask-app

CMD ["python3", "app.py"]