FROM python:3.8.13-slim

RUN mkdir /app \
        && apt-get update -y \
        && apt-get install -y --no-install-recommends \
            build-essential \
            libpq-dev \
            libsasl2-dev \
            libecpg-dev \
        && rm -rf /var/lib/apt/lists/*

COPY ./app.py /app/app.py
COPY ./oauthtest /app/oauthtest
COPY ./requirements.txt  /app/requirements/requirements.txt

RUN cd /app/requirements \
    && pip install --upgrade pip \
    && pip install --no-cache -r requirements.txt

WORKDIR /app

CMD ["python3", "app.py"]