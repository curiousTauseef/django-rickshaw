from django.apps import AppConfig


class RickshawConfig(AppConfig):
    name = 'rickshaw'
    verbose_name = "Rickshaw (Simple Cart Experience)"

    def ready(self):
        import rickshaw.signals
