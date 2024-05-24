from django.apps import AppConfig

class ClientprojectsConfig(AppConfig):
    """Configuration class for the clientprojects app.

    This AppConfig subclass represents the configuration for the clientprojects app.
    It specifies the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): The default auto field for models in this app.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientprojects'
