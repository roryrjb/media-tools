install: lint
	python3 setup.py install --user

lint:
	ruff check media_tools/

format:
	black media_tools/
