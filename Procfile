web: gunicorn --worker-tmp-dir /dev/shm sibyl:app
release: python manage.py makemigrations && python manage.py migrate