FROM python:alpine as base
RUN apk update && apk add gcc
RUN apk add musl-dev linux-headers libffi libffi-dev openssl-dev make

FROM base
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "app.py"]
