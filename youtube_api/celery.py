from __future__ import absolute_import, unicode_literals
import os

# This will make sure the app is always imported when
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtube_api.settings")
# Setting Celery app to app
app = Celery("youtube_api")
# Setting up namespace and settings to celery app
app.config_from_object("django.conf.settings", namespace="CELERY")
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
