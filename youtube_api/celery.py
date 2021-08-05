from __future__ import absolute_import,unicode_literals
import youtube_api.settings as settings
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','youtube_api.settings')

app = Celery('youtube_api')

app.config_from_object('django.conf.settings',namespace = 'CELERY')

app.autodiscover_tasks()