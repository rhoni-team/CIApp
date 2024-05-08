SHELL := /bin/bash
.ONESHELL:
VENV_FOLDER = env
DJANGO_PATH = AppCI
FRONTEND_PATH = AppCI/frontend
NVM_PATH_EXEC = ~/.nvm/nvm.sh

lint:
	source $(VENV_FOLDER)/bin/activate;
	pylint $(DJANGO_PATH)/backend $(DJANGO_PATH)/core_view $(DJANGO_PATH)/AppCI || true
