import os

import environ
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

env = environ.Env()
env.read_env(".env")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env.str("DJANGO_SETTINGS_MODULE"))

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.beat_schedule = {
    'multiply-task-crontab': {
        'task': 'multiply_two_numbers',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
    'multiply-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 5.0,
        'args': (16, 16)
    },
    'add-every-30-seconds': {
        'task': 'movies.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks(packages=settings.INSTALLED_APPS)
