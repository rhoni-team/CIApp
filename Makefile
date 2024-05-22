SHELL := /bin/bash
.ONESHELL:
VENV_FOLDER = env
DJANGO_PATH = AppCI
FRONTEND_PATH = AppCI/frontend
NVM_PATH_EXEC = ~/.nvm/nvm.sh
APP_DB = AppCI

lint:
	source $(VENV_FOLDER)/bin/activate;
	pylint $(DJANGO_PATH)/backend $(DJANGO_PATH)/core_view $(DJANGO_PATH)/AppCI || true

autopep:
	source $(VENV_FOLDER)/bin/activate;
	find . -name '*.py' \
		-not -path "*/frontend/node_modules/*" \
		-not -path "*/migrations/*" \
		-not -path "*/env/lib/*" \
		-exec autopep8 --in-place '{}' \;

test:
	source $(VENV_FOLDER)/bin/activate;
	cd $(DJANGO_PATH);
	python manage.py test

recreate-db:
	echo app db $(APP_DB)
	echo "DROP DATABASE \"$(APP_DB)\" WITH(FORCE);" | psql -d postgres
	echo "CREATE DATABASE \"$(APP_DB)\";" | psql -d postgres

new-migration-file:
	source $(VENV_FOLDER)/bin/activate;
	cd $(DJANGO_PATH);
	python manage.py makemigrations backend --empty
