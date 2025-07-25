# Generated by Django 5.0.6 on 2025-06-29 21:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_curso_cupos_disponibles_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Clave'),
        ),
    ]
