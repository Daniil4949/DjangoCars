FROM python:3.10.6-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR ..

RUN pip install pipenv
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY Pipfile .
COPY Pipfile.lock .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev --system --deploy
COPY . .
ENTRYPOINT ["../entrypoint.sh"]