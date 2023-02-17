web: gunicorn --worker-tmp-dir /dev/shm sibyl.wsgi
release: python manage.py makemigrations && python manage.py migrate