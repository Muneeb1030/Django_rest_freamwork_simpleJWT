# Django REST Framework Simple JWT Auth Project
## Overview
This project demonstrates the basics of Django REST Framework (DRF) and the implementation of JSON Web Token (JWT) authentication using the Simple JWT library. The main objectives of this project were to learn how to set up JWT authentication and to explore the usage of the `@api_view` decorator to create custom APIs.

## Features
- JWT Authentication using Simple JWT
- Custom APIs using @api_view
- Basic CRUD operations
- User authentication and authorization
## Getting Started
### Prerequisites
- Python 3.x
- Django
- Django REST Framework
- Simple JWT
### Installation
- Clone the repository:
```bash
https://github.com/Muneeb1030/Django_rest_freamwork_simpleJWT.git
cd Django_rest_freamwork_simpleJWT
```
- Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
- Install the dependencies:
```bash
pip install django djangorestframework djangorestframework-simplejwt
```
## Set up the Django project:

```bash
django-admin startproject myproject
cd myproject
```
 - Create a new app:

```bash
python manage.py startapp myapp
```
Add the new app and DRF to INSTALLED_APPS in settings.py:
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'myapp',
]
```
Configure DRF and Simple JWT in settings.py:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
}
```
- Create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
- Create a superuser:

```bash
python manage.py createsuperuser
```
## Usage
The project includes basic user authentication and authorization functionality, as well as custom APIs using the @api_view decorator. Users can register, log in, and perform CRUD operations on protected endpoints.

## Contributing
Contributions to the Django REST Framework Simple JWT Auth project are welcome! If you have any ideas, bug fixes, or enhancements, please open an issue or submit a pull request on the project's GitHub repository.

Contact
If you have any questions or suggestions regarding the Django REST Framework Simple JWT Auth project, please contact Me[muhammadmuneeburrehman.vercel.app]. Thank you for using this project!
