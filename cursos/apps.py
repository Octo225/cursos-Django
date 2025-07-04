from django.apps import AppConfig

class CursosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'CONVOCATORIAS'
    name = 'cursos'

class ActividadesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'ACTIVIDADES'
    name = 'Actividades'
    
