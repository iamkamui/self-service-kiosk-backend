migrate:
	python manage.py migrate $(app)
migrations:
	python manage.py makemigrations $(app)
show_urls:
	python manage.py show_urls
