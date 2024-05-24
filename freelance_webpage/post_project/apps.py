from django.apps import AppConfig

class PostProjectConfig(AppConfig):
    """Configuration class for the post_project app.

    This AppConfig subclass represents the configuration for the post_project app.
    It specifies the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): The default auto field for models in this app.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post_project'
