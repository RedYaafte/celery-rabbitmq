from django.apps import AppConfig


class MessagesConfig(AppConfig):
    name = 'messenger'

    def ready(self):
        import messenger.signals
