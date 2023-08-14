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

start:
	poetry run python manage.py runserver

migration:
	poetry run python manage.py makemigrations
