# User Password Reset

## Table of content

- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Setup](#setup)
- [Running the App](#running-the-app)


## Technologies
* Python 3.8.10
* Django 4.2.10
* Sqlite3

## Getting Started

### Installation

* Clone the repository
    ```
    https://github.com/micky225/Django-Password-Reset.git

    ```

### Setup

* To create a normal virtualenv (example .venv) and activate it (see Code below).

  ```
  virtualenv --python=python3.8.10 .venv
  
  source .venv/bin/activate

  (venv) $ pip install -r requirements.txt

  (venv) $ python manage.py makemigrations

  (venv) $ python manage.py migrate

  (venv) $ python manage.py createsuperuser 

  (venv) $ python manage.py runserver


## Running the App

```
http://127.0.0.1:8000/

```