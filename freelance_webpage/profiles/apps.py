from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"

    # Import signals when the app is ready
    def ready(self):
        import profiles.signals
