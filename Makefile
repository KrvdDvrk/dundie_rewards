.PHONY: installdev installtest virtualenv ipython clean test watch

install:
	@.venv/bin/python -m pip install -e .

installdev:
	@echo "Installing for dev enviroment"
	@pip install -r requirements_dev.text

installtest:
	@echo "Installing for test enviroment"
	@pip install -r requirements_test.txt

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -s

watch:
	# @.venv/bin/ptw
	ls **/*.py | entr pytest

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