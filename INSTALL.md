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
	- `docker-compose run --rm web /usr/local/bin/python manage.py loaddata users.yaml`
	- `docker-compose run --rm web /usr/local/bin/python manage.py loaddata product_groups.yaml`
	- `docker-compose run --rm web /usr/local/bin/python manage.py loaddata products.yaml`
6. Grab IP and point your browser to it
	- `docker-machine ip python-cafeen` - and view in your browser