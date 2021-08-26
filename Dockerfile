FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-2021-06-09

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app/