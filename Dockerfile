FROM python:3.6 as base
WORKDIR /app

# don't buffer python
ENV PYTHONUNBUFFERED 1
# don't create pyc
ENV PYTHONDONTWRITEBYTECODE 1

# create and permanently activate virtual environment
ENV VIRTUAL_ENV=/apt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y libpq-dev libjpeg-dev cron && apt-get autoclean
RUN pip install --upgrade pip && pip install wheel && pip install -r requirements.txt

COPY mudur mudur
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
COPY Dockerfile /Dockerfile

ENTRYPOINT ["./entrypoint.sh"]
CMD ["web"]
