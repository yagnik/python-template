help: ## display this help screen
	grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## setup python dependencies
	pipenv install --dev --deploy

test: ## run app tests
	pipenv run pytest --doctest-modules --cov=app/ --flake8 -v -p no:cacheprovider

shell: docker-start
	docker-compose -f build/docker-compose.yaml exec app pipenv shell

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
