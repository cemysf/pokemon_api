# Pokemon

This is a Pokemon API, implemented as a Django app.


## Quick start
-----------

0. Install app package

    pip install dist/django-pokemon-X.Y.tar.gz where X.Y is the version

1. Add "pokemon", "rest_framework" and "django_filters" to your INSTALLED_APPS setting like this::
    ```
    INSTALLED_APPS = [
        ...
        'pokemon',
        'rest_framework',
        'django_filters',
    ]
    ```
2. Include the pokemon URLconf in your project urls.py like this::
    ```
    path('pokemon/', include('pokemon.urls')),
    ```
3. Run ``python manage.py migrate`` to create the pokemon models.

4. Add following to project setting for pagination
    ```
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10"
    }
    ```

