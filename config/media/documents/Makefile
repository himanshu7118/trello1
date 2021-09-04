manage=./manage.py
python=python3

runserver-plus:
	$(python) $(manage) runserver_plus 
	
runserver:
	$(python) $(manage) runserver 


check:
	$(python) $(manage) check 


initial-setup: 
	pip install -r requirements.txt

shell:
	$(python) $(manage) shell_plus 
	
superuser:
	$(python) $(manage) createsuperuser 
	

migrate:
	$(python) $(manage) makemigrations && $(python) $(manage) migrate

freeze:
	pip freeze > requirements.txt


user:
	$(python) $(manage) demo_user

create-data:
	$(python) $(manage) create_data

delete-data:
	$(python) $(manage) delete_data


data:
	make user
	make create-data


