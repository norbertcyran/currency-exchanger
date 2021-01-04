FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install poetry==1.1.2

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev libpq-dev \
    && poetry install \
    && apt-get purge -y gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

CMD ["gunicorn", "--workers=5", "--bind=0.0.0.0:8000", "currency_exchanger.wsgi:application"]