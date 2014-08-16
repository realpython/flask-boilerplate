.PHONY: virtualenv

ENV = development
PYTEST_OPTIONS = -vv --exitfirst -n 8
VENV = config/$(ENV)/env
export PYTHONPATH := $(PYTHONPATH):.

# Run a local web server
server: $(VENV)
	. $(VENV)/bin/activate; python run.py

config/%/env: config/%/requirements.txt
	virtualenv $@
	. $@/bin/activate && pip install --requirement $<

shell:
	python shell.py

test: $(VENV)
	. $(VENV)/bin/activate; py.test $(PYTEST_OPTIONS) tests/
