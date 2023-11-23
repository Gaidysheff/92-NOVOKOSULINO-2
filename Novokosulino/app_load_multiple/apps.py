from django.apps import AppConfig


class AppLoadMultipleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_load_multiple'
    verbose_name = 'Загруженные файлы Multiple'
