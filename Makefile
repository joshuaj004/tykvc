env:
	@python3 -m venv env

####################
# run local server
####################
server:
	@FLASK_APP=run.py flask run

server-debug:
	@$(shell FLASK_DEBUG=1 make server)


####################
# dependencies
####################
deps:
	@pip install -r requirements.txt

deps-update:
	@pip install -r requirements-to-freeze.txt --upgrade
	@pip freeze > requirements.txt

deps-uninstall:
	@pip uninstall -yr requirements.txt
	@pip freeze > requirements.txt


####################
# lint
####################
lint:
	@pre-commit run \
		--allow-unstaged-config \
		--all-files \
		--verbose

autopep8:
	@autopep8 . --recursive --in-place --pep8-passes 2000 --verbose

autopep8-stats:
	@pep8 --quiet --statistics .

.PHONY: deps* lint autopep8* server*
