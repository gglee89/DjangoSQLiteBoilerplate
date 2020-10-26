# About this project

**Django + CELERY + SQLite Boilerplate.**

The intent of this project is to:

1. Validate the options in regards to how we can manage SQLite migration and CRUD from a Django application perspective.
2. Validate the integration of Instaloader with Celery

# Dependencies

```python
# Setup Celery
https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html

# Setup RabbitMQ or Redis as a SERVICE
https://www.rabbitmq.com/download.html
```

# How to start:

```python
# Install Module Dependencies
pip install requirements.txt
```

```python
# In one terminal tab
# Start the django application
python manage.py runserver
```

```python
# In another terminal tab
# Start celery
celery -A digimarket_test worker --pool=eventlet -l INFO
```

# References:

```js
/digimarket_test
  manage.py
  /digimarket_test
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
  /code
    /migrations
    /static // Static files
    /templates // Django template filees
    __init__.py
    admin.py
    apps.py
    forms.py
    modles.py
    tasks.py // Celery Task
    tests.py
    urls.py // Django endpoint/route setup
    views.py // View Renderer
```
