python manage.py collectstatic --noinput
python manage.py migrate --noinput 
gunicorn resume_project.wsgi:application --bind 0.0.0.0:$PORT