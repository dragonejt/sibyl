web: gunicorn --worker-tmp-dir /dev/shm sibyl/wsgi.py
release: python manage.py makemigrations && python manage.py migrate