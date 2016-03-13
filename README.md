# Cafeen Stock Control System

## Environment
- Docker v1.9.1
- Docker Compose v1.5.2
- Docker Machine v0.5.4
- Python 3.5
- Postgres
- Nginx

### Setup Instructions

1. Install docker
	- `brew cask install dockertoolbox`
2. Start new machine
	- `docker-machine create -d virtualbox python-cafeen`
	- `eval "$(docker-machine env python-cafeen)"`
3. Build and start containers
	- `docker-compose build`
	- `docker-compose up -d`
5. Create migrations and root user
	- `docker-compose run --rm web /usr/local/bin/python manage.py migrate`
	- `docker-compose run --rm web python manage.py createsuperuser`
6. Grab IP and point your browser to it
	- `docker-machine ip python-cafeen` - and view in your browser

## Testing

We're using Behave for acceptance tests. The tests can be run with:

`docker-compose run --rm web behave ./cafe/features/stock`

For testing emails all emails are saved to files in `/web/cafe/var/email`.