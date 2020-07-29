release: sh -c 'cd ./myproject && python manage.py migrate'
web: sh -c 'cd ./myproject && gunicorn myproject.wsgi --log-file -'
