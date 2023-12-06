FROM python:3.10

WORKDIR /tasks

COPY ./requirements.txt /tasks/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tasks/requirements.txt

COPY ./app /tasks/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
