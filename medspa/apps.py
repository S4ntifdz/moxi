from django.apps import AppConfig


class MedspaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "medspa"
    
    def ready(self):
        import medspa.signals.pre_save_service_signal