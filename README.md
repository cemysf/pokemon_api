# pokemon_api
## Summary

My implementation of a Pokemon API as a Django app.

For decoupling and re-usability, the django app is created inside django_pokemon folder with a PyPI formatted setup configuration.

---

## Features
### List view (paginated)

`http://127.0.0.1:8000/pokemon/`

`http://127.0.0.1:8000/pokemon/?page=3`

### Search

`http://127.0.0.1:8000/pokemon/?search=Charmander` should return one pokemon

`http://127.0.0.1:8000/pokemon/?search=saur` returns pokemons with "saur" in the name, such as "Bulbasaur", "Ivysaur"..

### Filter

`http://127.0.0.1:8000/pokemon/?hp__gte=45&attack__lte=30&defense=35` returns "Caterpie", "Smeargle" and "Spoink"


---
## How to?
### Setup Environment
#### Option 1: Using scripts
I wrote some scripts to automate creating and setting up a python virtual environment and a django project.

1. First, run this script to create a python virtual environment, install requirements and create a dummy django project. This will create new folders _virtualenv_ and _dummyproject_.
    ```
    ./create_project_environment.sh
    ```
2. Activate the newly created virtual environment for the rest of the steps.
    ```
    source ./virtualenv/bin/activate
    ```
3. Then, change directory into django-pokemon folder and create source distribution. This will create a *django-pokemon-X.Y.tar.gz* file _django-pokemon/dist_ folder, where X,Y is the version number specified in _django-pokemon/setup.cfg_
    ```
    cd django-pokemon
    ./package_dist.sh
    ```
4. Go to upper directory, run other script for setting up django project and db migrations.
    ```
    cd ..
    ./setup_project_environment.sh
    ```
#### Option 2: Without using scripts
1. Include django-pokemon to your django project (see _django-pokemon/README.md_)
### Run Server
- Inside the django project folder, run following
    ```
    python manage.py runserver
    ```
### Run Tests
- Inside the django project folder, run following
    ```
    python manage.py test pokemon
    ```
