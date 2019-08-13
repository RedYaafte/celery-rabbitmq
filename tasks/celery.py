from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.core.mail import send_mail
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasks.settings')

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# print('zona default ', app.conf.timezone)
# app.conf.timezone = 'America/Mexico_City'
# print('Nueva configuración ', app.conf.timezone)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, test.s('<---  hello'), name='add every 10s')

    # Send email every 90 seconds
    sender.add_periodic_task(10.0, send_mail_task.s('Send mail :D'),
                             mame='add every 10s')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world  --->'), name='add every 30s')

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=17, minute=45, day_of_week=2),
        test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)


@app.task
def send_mail_task(arg):
    send_mail(
        'Celery mola!!',
        'Here is the message.   :D',
        os.environ['EMAIL_HOST_USER'],
        [os.environ['EMAIL_RECIBE']],
        fail_silently=False,
    )
    return "Nice!!"


@app.task(bind=True)
def debug_task(self):
    print('Debug task ------>')
    print('Request: {0!r}'.format(self.request))
