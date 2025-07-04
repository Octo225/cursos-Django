from django.db import models
from ckeditor.fields import RichTextField


class Curso(models.Model):
    id= models.AutoField(primary_key=True,verbose_name="Clave")
    titulo = models.CharField(max_length=200, verbose_name="Titulo del curso")
    descripcion = models.TextField(verbose_name="Descripcion del curso")
    nivel = models.CharField(max_length=50, verbose_name="Nivel del curso(Principiante/Intermedio/Avanzado)")
    duracion_semanas = models.PositiveIntegerField(verbose_name="Duracion del curso(Semanas)")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio del curso en MXN")
    cupos_disponibles = models.IntegerField(verbose_name="Cupos disponibles")
    estado = models.CharField(max_length=50, verbose_name="Estado del curso(disponible/completo/cancelado)")
    imagen = models.ImageField(upload_to='cursos/fotos', verbose_name="Imagen del curso")
    es_certificado = models.BooleanField(default=False, verbose_name="Esta certificado?")
    profesor = models.CharField(max_length=100, verbose_name="Profesor asignado")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['fecha_creacion']
    
    def __str__(self):
        return self.titulo
    
class Actividad(models.Model):
    id= models.AutoField(primary_key=True,verbose_name="Clave")
    curso= models.ForeignKey(Curso,on_delete=models.CASCADE,verbose_name="Curso")
    descripcion=RichTextField(verbose_name="Descripcion de actividad")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    fecha_modificacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['fecha_creacion']
    
    def __int__(self):
        return self.id

