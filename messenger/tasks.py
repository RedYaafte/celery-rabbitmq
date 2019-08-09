from __future__ import absolute_import, unicode_literals
from celery import Celery, shared_task

from tasks.celery import app


# @app.task
@shared_task
def summ(x, y):
    return x + y


# @app.task
@shared_task
def multiplicate(x, y):
    return x * y


# @shared_task
# def count_messages():
#     return Message.objects.all().count()
