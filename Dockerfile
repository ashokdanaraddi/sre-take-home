FROM python:3.10-alpine

WORKDIR /src

ADD user_hasher user_hasher
ADD requirements requirements

RUN pip install --upgrade pip wheel setuptools -r requirements/requirements-prod.txt

ENTRYPOINT ["uvicorn", "user_hasher.main:app", "--host=0.0.0.0", "--port=8000"]
