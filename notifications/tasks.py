from __future__ import absolute_import, unicode_literals
from tasks.celery import app
from .models import ConfigurationNotification


@app.task
def test_time(type):
    print("type", type, flush=True)
    return type


@app.task
def test_condition(condition):
    print("test_condition -->", condition, flush=True)
    return {'status': 200}
