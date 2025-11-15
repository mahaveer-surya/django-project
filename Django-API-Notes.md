# Django API Development
1. create vitual environment

2. create a django project
```
django-admin startproject project_name
Ex.
django-admin startproject django_rest_api_main
``` 

3. install django rest framework and configure it the project
a) Intstall the drf
```python 
pip install djangorestframework
```
b) add the drf in apps under setting.py


There is two types of Endpoints
1) Web Application Endpoints
users can directly access it from the web browsers

https://127.0.0.1:8000/students/
2) API Endpoints
Return the data to integrate into the frontend.
https://127.0.0.1:8000/api/v1/students/


# How to create the superuser 
```
python manage.py createsuperuser
```