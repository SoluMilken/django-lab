.DEFAULT_GOAL := all

.PHONY: install
install:
	pipenv install --dev

.PHONY: lint
lint:
	flake8 .

.PHONY: test
test:
	python ./mysite/manage.py test polls

.PHONY: all
all: lint test
