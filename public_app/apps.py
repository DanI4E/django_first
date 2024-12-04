from django.apps import AppConfig


class PublicAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'public_app'

    def ready(self):
        # для импорта сигналов

        from . import signals

