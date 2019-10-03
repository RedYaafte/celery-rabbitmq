from django.db import models
from django.conf import settings


class Message(models.Model):
    """
    Message model.
    """

    EVENT_TYPE = 0
    NOTICE_TYPE = 1

    CRITICAL_PRIORITY = 0
    IMPORTANT_PRIORITY = 1
    NORMAL_PRIORITY = 2
    LOW_PRIORITY = 3

    TYPE_CHOICES = (
        (EVENT_TYPE, 'Evento'),
        (NOTICE_TYPE, 'Aviso')
    )

    PRIORITY_CHOICES = (
        (CRITICAL_PRIORITY, 'Critico'),
        (IMPORTANT_PRIORITY, 'Importante'),
        (NORMAL_PRIORITY, 'Normal'),
        (LOW_PRIORITY, 'Baja')
    )

    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES, default=NOTICE_TYPE)
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES, default=NORMAL_PRIORITY)
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='messages_sent', null=True)
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='messages',
        null=True,
        blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    read = models.BooleanField(default=False)
    event = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
