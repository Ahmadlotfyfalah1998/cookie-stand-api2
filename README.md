## LAB - Class 34
## Project: Putting it All Together
## Author: ahmad falah
## Links and Resources
- username=ahmad
- password=0000
## Setup
## .env requirements (where applicable)


- SECRET_KEY=HQ0btsevDqakviMqRdmpE5FD2y7MvwrUA7U7u1M66Ls
- DEBUG=True

- ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
- ALLOW_ALL_ORIGINS=True

- DATABASE_ENGINE=django.db.backends.postgresql
- DATABASE_NAME=wgzfelar
- DATABASE_USER=wgzfelar
- DATABASE_PASSWORD=JiXC_W8F0LjOMEvkauPvWAGFV6QMCFyD
- DATABASE_HOST=peanut.db.elephantsql.com
- DATABASE_PORT=5432


## PORT - 8000
## DATABASE_URL - URL to the running Postgres instance/db
- postgres://wgzfelar:JiXC_W8F0LjOMEvkauPvWAGFV6QMCFyD@peanut.db.elephantsql.com/wgzfelar
## How to initialize/run your application (where applicable)
- docker compose up 










# api-quick-start

Template Project for starting up CRUD API with Django Rest Framework

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `Book` folder to the app name of your choice
- Search through entire code base for `Book`,`Book` and `Book` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
  - "Front" files
    - if including a customer facing portion of the site then update/recreate:
      - `urls_front.py`
      - `views_front.py`
      - template files
      - Make sure to update project `urls.py` to add routes to the "front".
- Update BookModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.
- Run `python manage.py collectstatic`
  - This repository includes static assets in repository. If you are using a Content Delivery Network then remove `staticfiles` from repository.
- Optional: Update `api_tester.py`

## Database

**NOTE:** If you are using Postgres instead of SQLite then make sure to install `psycopg2-binary` and include in `requirements.txt`
