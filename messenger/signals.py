from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Message
from messenger.tasks import multiplicate
from notifications.tasks import test_time, test_condition
from notifications.models import ConfigurationNotification

User = get_user_model()


@receiver(post_save, sender=Message)
def create_notification(sender, instance=None, created=False, **kwargs):
    """
    Added type in task
    """

    if created:
        event = ConfigurationNotification.objects.filter(
            type=instance.event).values(
                'pk', 'type', 'time', 'condition').first()
        print("event ---->", event, flush=True)

        if event['time']:
            print("time", flush=True)
            test_time.delay(event)
        if event['condition']:
            print("condition", flush=True)
            test_condition.delay(event)
