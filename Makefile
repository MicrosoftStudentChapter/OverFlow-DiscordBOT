requirements: requirements.txt requirements-dev.txt

requirements.txt: pyproject.toml poetry.lock
	poetry export --format requirements.txt --output requirements.txt --without-hashes

requirements-dev.txt: pyproject.toml poetry.lock
	poetry export --format requirements.txt --output requirements-dev.txt --without-hashes --dev
