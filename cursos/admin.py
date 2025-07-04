from django.contrib import admin
from .models import Curso
from .models import Actividad


class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nivel', 'estado', 'duracion_semanas', 'precio', 'fecha_creacion', 'imagen','profesor')
    list_filter = ('nivel', 'estado', 'es_certificado')
    search_fields = ('titulo', 'descripcion', 'profesor')
    
admin.site.register(Curso, CursoAdmin)

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id','curso', 'descripcion', 'fecha_creacion')
    search_fields = ('titulo','id')
    
admin.site.register(Actividad, ActividadAdmin)
