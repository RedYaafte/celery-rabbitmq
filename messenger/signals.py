from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Message

User = get_user_model()


@receiver(post_save, sender=Message)
def create_notification(sender, instance=None, created=False, **kwargs):
    print("pass", flush=True)
    pass
