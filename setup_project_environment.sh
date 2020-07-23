#!/usr/bin/env bash
VENV_PATH='virtualenv'
PROJ_PATH='dummyproject'

source ./$VENV_PATH/bin/activate

# install app package
python -m pip install django-pokemon/dist/django-pokemon-0.1.tar.gz

# make changes
sed -i '/INSTALLED_APPS = \[/a "pokemon",\n"rest_framework",\n"django_filters",' $PROJ_PATH/$PROJ_PATH/settings.py
sed -i '/urlpatterns = \[/a path("pokemon/", include("pokemon.urls")),' $PROJ_PATH/$PROJ_PATH/urls.py
sed -i '/urlpatterns = \[/i from django.urls import include' $PROJ_PATH/$PROJ_PATH/urls.py

# pagination
echo "REST_FRAMEWORK = {" >> $PROJ_PATH/$PROJ_PATH/settings.py
echo "    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'," >> $PROJ_PATH/$PROJ_PATH/settings.py
echo "    'PAGE_SIZE': 10" >> $PROJ_PATH/$PROJ_PATH/settings.py
echo "}" >> $PROJ_PATH/$PROJ_PATH/settings.py

# init models
python $PROJ_PATH/manage.py migrate
