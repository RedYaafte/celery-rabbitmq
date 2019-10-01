from django.db import models


class ConfigurationNotification(models.Model):
    """
    Configure notifications, web push notifications and messages
    """

    HIGH = 0
    MEDIUM = 1
    LOW = 2

    CONDITION_CHOICES = (
        (HIGH, 'Alto'),
        (MEDIUM, 'Medio'),
        (LOW, 'Bajo')
    )

    time = models.DateField(blanck=True, null=True)
    condition = models.PositiveSmallIntegerField(
        choices=CONDITION_CHOICES, default=MEDIUM)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
