web: flask db upgrade; flask translate compile; gunicorn pyweb:app
worker: rq worker -u $REDIS_URL pyweb-tasks