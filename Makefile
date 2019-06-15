docker-compose:
	@docker-compose version

docker-start: docker-compose
	docker-compose -f build/docker-compose.yaml up -d

docker-clean: docker-compose
	docker-compose -f build/docker-compose.yaml down
	docker-compose -f build/docker-compose.yaml rm

docker-rebuild: docker-compose ## rebuild docker containers of the project
	docker-compose -f build/docker-compose.yaml build

docker-setup: docker-start ## setup salt with docker containers for testing
	docker-compose -f build/docker-compose.yaml exec app make setup

docker-test: docker-setup ## run salt tests inside container
	docker-compose -f build/docker-compose.yaml exec app make test

setup: ## setup python dependencies
	pipenv install --dev --deploy

test-style: ## test all style check
	pipenv run flake8 .

test-app: ## run app tests
	pipenv run pytest -v -p no:cacheprovider

test: test-app ## run all tests

shell: docker-start
	docker-compose -f build/docker-compose.yaml exec app pipenv shell

help: ## display this help screen
	grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
