FROM python:3.10

WORKDIR /gateway

COPY ./requirements.txt /gateway/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /gateway/requirements.txt

COPY ./app /gateway/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
