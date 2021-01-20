# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:alpine

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Build and install libpostal
WORKDIR /usr/src
RUN apk update && apk add git curl autoconf automake libtool pkgconfig make g++ && \
    git clone https://github.com/openvenues/libpostal && cd libpostal && \
    sed -i 's/ -P $NUM_WORKERS//' src/libpostal_data.in && mkdir /data && \
    ./bootstrap.sh && ./configure --datadir=/data && make && make install && \
    apk del --purge git autoconf automake libtool pkgconfig make curl && \
    cd && rm -rf /usr/src/libpostal

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN addgroup -S django && adduser -S django -G django && chown -R django /app
USER django

RUN python manage.py collectstatic --no-input --clear

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hello_app.wsgi"]
