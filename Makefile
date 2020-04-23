define with_docker
	docker-compose -p server_devcontainer -f .devcontainer/docker-compose.yaml $(1)
endef

help: ## display this help screen
	grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## setup python dependencies
	poetry install --no-root

test: ## run app tests
	poetry run pytest

test-html: ## run app tests with http coverage report
	poetry run pytest  --cov-report=html:tmp/htmlcov

shell: docker-start ## get in shell where app
	$(call with_docker, exec template poetry run /bin/bash)

docker-compose:
	@docker-compose version

docker-start: docker-compose
	$(call with_docker, up -d)

docker-clean: docker-compose
	$(call with_docker, down)
	$(call with_docker, rm)

docker-rebuild: docker-compose ## rebuild docker containers of the project
	$(call with_docker, build)

docker-setup: docker-start ## setup salt with docker containers for testing
	$(call with_docker, exec template make setup)

docker-test: docker-setup ## run salt tests inside container
	$(call with_docker, exec template make test)
