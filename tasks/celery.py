from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.core.mail import send_mail
import os
import smtplib

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasks.settings')

app = Celery('proj')
app.conf.update(enable_utc=True, timezone='America/Mexico_City')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, test.s('<---  hello'), name='add every 10s')

    # Send email
    sender.add_periodic_task(
        crontab(hour=11, minute=18),
        send_email_smpt.s('Mail send --> :D'),
        mame='mailing'
    )

    sender.add_periodic_task(
        crontab(hour=15, minute=1, day_of_week='friday'),
        test.s('Happy Mondays!'),
        name='add every hour'
    )


@app.task
def test(arg):
    print("<----- Test ----->", arg, flush=True)
    return print("Enjoy Docker!! ---------->", flush=True)


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


@app.task
def send_email_smpt(self):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hello from Mandrill, Python style!"
    msg['From'] = os.environ['EMAIL_HOST_USER']
    msg['To'] = os.environ['EMAIL_RECIBE']

    text = "Mandrill speaks plaintext"
    part1 = MIMEText(text, 'plain')

    html = "<em>Mandrill speaks <strong>HTML</strong></em>"
    part2 = MIMEText(html, 'html')

    username = settings.MANDRILL_USERNAME
    password = settings.MANDRILL_APIKEY

    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP('smtp.mandrillapp.com', 587)

    s.login(username, password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    print(s)

    s.quit()


@app.task(bind=True)
def debug_task(self):
    print('Debug task ------>')
    print('Request: {0!r}'.format(self.request))
