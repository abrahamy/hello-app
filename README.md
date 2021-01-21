# Hello App

A demo app for parsing addresses. Given a street address like "Alexanderplatz 75" will return the
dictionary `{"street": "Alexanderplatz", "housenumber": 75}`.

## Dependencies

- Python 3.8+
- [libpostal](https://github.com/openvenues/libpostal)
- [postal](https://github.com/openvenues/pypostal) - Python bindings for libpostal
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [gunicorn](https://gunicorn.org/)
- [Docker](https://www.docker.com/)

### Dev Dependencies

- Pytest
- Pytest-Django

# Getting Started

Clone this repository onto your computer and run the following commands to build and start the application.

```
git clone https://github.com/abrahamy/hello-app.git
cd hello-app
docker build -t helloapp .
docker run --rm helloapp
```

The application is now running on localhost at port 8000.

## Running unit tests

Run unit tests with this command `docker run --rm helloapp pytest`

## Using the parser directly

Launch the python interactive shell by running `docker run -it --rm helloapp python`. The parser can be called as shown below.

![Usage](https://github.com/abrahamy/hello-app/blob/main/example.png?raw=true)

_Note_
\_To run on your computer without using docker you need to ensure that the above dependencies are install. You may need to
add `export LD_LIBRARY_PATH=/usr/local/lib` in your `.zshrc` or `.bashrc`. Alternatively, you may prefix your commands like
so `LD_LIBRARY_PATH=/usr/local/lib python`.
