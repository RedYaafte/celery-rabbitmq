from django.contrib import admin
from .models import ConfigurationNotification


@admin.register(ConfigurationNotification)
class MessageAdmin(admin.ModelAdmin):
    """
    Model admin for ConfigurationNotification model.
    """

    pass
