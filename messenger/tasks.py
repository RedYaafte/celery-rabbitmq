from __future__ import absolute_import, unicode_literals
from django.utils import timezone
from celery import Celery, shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from tasks.celery import app
import django
django.setup()


# @app.task
@shared_task
def summ(x, y):
    return f"Resultado {x + y}"


# @app.task
@shared_task
def multiplicate(x, y):
    return x * y


@shared_task
def count_messages():
    from django.contrib.auth.models import User
    from .models import Message
    user = User.objects.first()
    fake_id = Message.objects.all().count()
    message = Message.objects.create(
        type=Message.NOTICE_TYPE,
        priority=Message.NORMAL_PRIORITY,
        from_user=user,
        to_user=user,
        title=f'Test {fake_id + 1}',
        body=f'Test {fake_id + 1}'
    )

    return f"Nuevo mensage envíado con id: {message.id}"


@app.task
def test_configuration(x, y):
    print(x + y)
