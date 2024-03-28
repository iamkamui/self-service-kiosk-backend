.PHONY: start
start: migrate
	docker compose up -d

.PHONY: migrate
migrate:
	docker compose run --rm django python manage.py migrate $(app)

.PHONY: migrations
migrations:
	docker compose run --rm django python manage.py makemigrations $(app)

.PHONY: show_urls
show_urls: up
	docker compose run --rm django python manage.py show_urls
