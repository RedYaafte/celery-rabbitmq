from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasks.settings')

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))