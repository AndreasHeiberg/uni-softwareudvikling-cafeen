# Cafeen Stock Control System

## Environment
- Docker v1.9.1
- Docker Compose v1.5.2
- Docker Machine v0.5.4
- Python 3.5
- Postgres
- Redis
- Nginx

Blog post -> https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/

### OS X Instructions

1. Start new machine - `docker-machine create -d virtualbox python-cafeen`
2. `eval "$(docker-machine env python-cafeen)"`
3. Build images - `docker-compose build`
4. Start services - `docker-compose up -d`
5. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate`
6. Grab IP - `docker-machine ip python-cafeen` - and view in your browser

docker-compose run web python manage.py createsuperuser

## Testing

We're using Behave for acceptance tests. The tests can be run with:

`docker-compose run web behave ./docker_django/features/stock`

python -m smtpd -n -c DebuggingServer localhost:1025

## Products

## Product Groups