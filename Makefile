

run.local:
	python src/manage.py runserver

run.shell:
	python src/manage.py shell_plus

migrations:
	python src/manage.py makemigrations

migrate:
	python src/manage.py migrate