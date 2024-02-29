FROM python:3.7-slim

RUN mkdir project

WORKDIR fastapi

ADD . /fastapi/
ADD .env /fastapi/.env

RUN pip install -r requirements.txt
EXPOSE 5432

CMD ["uvicorn", "main:app", "--reload",  "--host", "0.0.0.0", "--port", "8000"]