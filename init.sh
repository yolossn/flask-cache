service memcached start
gunicorn --workers 10 --bind 0.0.0.0:5000 --log-level DEBUG wsgi:app

