# finn_repo

My implementation of a Pokemon API using Django framework

## How to run?
### 1. Setup Environment
I wrote some scripts to automate creating and setting up a python virtual environment.

1. First, run this script to create a python virtual environment, install requirements and create a dummy django project.
    ```
    ./create_project_environment.sh
    ```
* Activate the newly created virtual environment for the rest of the steps.
    ```
    source ./virtualenv/bin/activate
    ```
* Then, change directory into django-pokemon folder and create source distribution.
    ```
    cd django-pokemon
    ./package_dist.sh
    ```
* Go to upper directory, run other script for setting up django project and db migrations.
    ```
    ./setup_project_environment.sh
    ```


