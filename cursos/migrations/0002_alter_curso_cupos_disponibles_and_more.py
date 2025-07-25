# Generated by Django 5.0.6 on 2025-06-29 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='cupos_disponibles',
            field=models.IntegerField(verbose_name='Cupos disponibles'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion del curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='duracion_semanas',
            field=models.PositiveIntegerField(verbose_name='Duracion del curso(Semanas)'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='es_certificado',
            field=models.BooleanField(default=False, verbose_name='Esta certificado?'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='estado',
            field=models.CharField(max_length=50, verbose_name='Estado del curso(disponible/completo/cancelado)'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(upload_to='cursos/fotos', verbose_name='Imagen del curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(max_length=50, verbose_name='Nivel del curso(Principiante/Intermedio/Avanzado)'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Precio del curso en MXN'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo del curso'),
        ),
    ]
