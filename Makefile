migrate:
	docker compose run --rm api python manage.py migrate

migrations:
	docker compose run --rm api python manage.py makemigrations $(app)

show_urls:
	docker compose run --rm api python manage.py show_urls
