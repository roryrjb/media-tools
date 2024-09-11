install: lint
	python setup.py install --user

lint:
	ruff check media_tools/

format:
	black media_tools/
