migrate:
	docker compose run --rm api python manage.py migrate

show_urls:
	docker compose run --rm api python manage.py show_urls