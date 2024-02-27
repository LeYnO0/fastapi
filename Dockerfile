FROM python:3.7-slim

RUN mkdir project

WORKDIR project

ADD . /project/
ADD .env /project/.env

RUN pip install -r requirements.txt
RUN cd /project

#RUN ufw allow 5444
#RUN alembic revision --autogenerate
#RUN alembic upgrade head

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]