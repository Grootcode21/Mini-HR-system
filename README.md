~ pip install virtualenv
~ virtualenv myenv
~ myenv\scripts\activate

> pip install django django-ckeditor djangorestframework six pillow 

# check versions
pip show django
python -m django --version
pip --version
python --version

django-admin startproject project_name .
python manage.py startapp app_name 


create urls.py inside the app
create a folder named templates inside the app
inside that templates create a folder named app_name - put in all static files e.g index.html

python manage.py showmigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate