.PHONY: install installdev installtest virtualenv ipython pflake8 fmt clean test watch

install:
	@.venv/bin/python -m pip install -e .

installdev:
	@echo "Installing for dev enviroment"
	@.venv/bin/python -m pip install -e .[dev]

installtest:
	@echo "Installing for test enviroment"
	@.venv/bin/python3 -m pip install -e .[test]

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort dundie tests integration
	@.venv/bin/black dundie tests integration

test:
	@.venv/bin/pytest -s

watch:
	# @ls **/*.py | entr pytest

clean:
	@find ./ - name '*.pyc' -exec rm -f {} \;
	@find ./ '__pycache__' -exec rm -rf {} \;
	@find ./ 'Thumbs.db' -exec rm -rf {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
