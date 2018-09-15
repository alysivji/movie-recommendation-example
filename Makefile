help:
	@echo 'Makefile for managing web application                        '
	@echo '                                                             '
	@echo 'Usage:                                                       '
	@echo ' make build      build images                                '
	@echo ' make up         creates containers and starts service       '
	@echo ' make start      starts service containers                   '
	@echo ' make stop       stops service containers                    '
	@echo ' make down       stops service and removes containers        '
	@echo '                                                             '
	@echo ' make migrate    run migrations                              '
	@echo ' make test       run tests                                   '
	@echo ' make test_cov   run tests with coverage.py                  '
	@echo ' make test_fast  run tests without migrations                '
	@echo ' make lint       run flake8 linter                           '
	@echo '                                                             '
	@echo ' make attach     attach to process inside service            '
	@echo ' make logs       see container logs                          '
	@echo ' make shell      connect to app container in new bash shell  '
	@echo ' make dbshell    connect to postgres inside db container     '
	@echo '                                                             '

build:
	docker-compose build

up:
	docker-compose up -d
	make migrate-up

start:
	docker-compose start

stop:
	docker-compose stop

down:
	docker-compose down

attach: ## Attach to web container
	docker attach `docker-compose ps -q app`

logs:
	docker logs `docker-compose ps -q app`

shell: ## Shell into web container
	docker-compose exec app bash

shell-db: ## Shell into postgres process inside db container
	docker-compose exec db psql -w --username "sivpack" --dbname "sivdev"

shell-flask:
	docker-compose exec app flask konch

shell-root:  # Shell into web container as root
	docker-compose exec -u root app bash

migration: ## Create migrations using flask migrate
	docker-compose exec app flask db migrate -m "$(m)"

migrate-up: ## Run migrations using flask migrate
	docker-compose exec app flask db upgrade

migrate-down: ## Rollback migrations using flask migrate
	docker-compose exec app flask db downgrade

test: migrate-up
	docker-compose exec app pytest

test-cov: migrate-up
	docker-compose exec app pytest --verbose --cov

test-cov-view: migrate-up
	docker-compose exec app pytest --cov --cov-report html && open ./htmlcov/index.html

test-fast: ## Can pass in parameters using p=''
	docker-compose exec app pytest $(p)

# Flake 8
# options: http://flake8.pycqa.org/en/latest/user/options.html
# codes: http://flake8.pycqa.org/en/latest/user/error-codes.html
max_line_length = 99
lint: up
	docker-compose exec app flake8 \
		--max-line-length $(max_line_length)
