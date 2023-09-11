install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8

test:
	poetry run python3 manage.py test

test-coverage:
	coverage run --source='.' manage.py test
	coverage report

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

translate:
	django-admin makemessages -l ru

trans-complete:
	django-admin compilemessages

migration:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

shell:
	python manage.py shell
