.PHONY: clean help \
	quality requirements selfcheck test upgrade

.DEFAULT_GOAL := help

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

requirements: ## install development environment requirements
	pip install -r requirements.txt


# test: ## run unitary tests and meassure coverage
# 	coverage run --source=models -m pytest
# 	coverage report -m --fail-under=62

# quality: ## check coding style with pycodestyle and pylint
# 	pylint commands *.py
# 	pycodestyle commands *.py
# 	pydocstyle commands *.py
# 	pylint models *.py
# 	isort --check-only --diff models *.py
# 	python setup.py bdist_wheel
# 	make selfcheck

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."

# example: ## run a example of the simulator
# 	genIdenti
