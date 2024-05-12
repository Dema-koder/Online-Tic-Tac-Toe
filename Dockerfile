# Stage1: Base build
FROM python:3.9-alpine as base
WORKDIR /usr/src/app
RUN apk add --update --virtual .build-deps \
    build-base \
    python3-dev
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Stage 2: Production stage
FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY --from=base /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY . /usr/src/app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]