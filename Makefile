dependencies:
	pip install -r requirements.txt

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

create-user: 
	python manage.py createsuperuser

runserver:
	python manage.py runserver
