#!/usr/bin/env bash
VENV_PATH='virtualenv'
PROJ_PATH='dummyproject'

# cleanup folders if exist 
[ -d "$VENV_PATH" ] && { rm -rf $VENV_PATH;echo "Removed old folder $VENV_PATH"; } 
[ -d "$PROJ_PATH" ] && { rm -rf $PROJ_PATH;echo "Removed old folder $PROJ_PATH"; } 

# create virtual env
python3 -m venv $VENV_PATH
source ./$VENV_PATH/bin/activate

# install requirements
python3 -m pip install -r requirements.txt

# create a django dummy project
django-admin startproject $PROJ_PATH


