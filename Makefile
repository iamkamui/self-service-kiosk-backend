.PHONY: start
start:
	docker compose up -d
	make migrate

.PHONY: migrate
migrate:
	docker compose run --rm django python manage.py migrate $(app)

.PHONY: migrations
migrations:
	python manage.py makemigrations $(app)

.PHONY: show_urls
show_urls:
	docker compose run --rm django python manage.py show_urls

superuser:
	docker compose run --rm django python manage.py createsuperuser

.PHONY: test
test:
	docker compose run --rm django python manage.py test $(path) --keepdb

.PHONY: shell_plus
shell_plus:
	docker compose run --rm django python manage.py shell_plus
