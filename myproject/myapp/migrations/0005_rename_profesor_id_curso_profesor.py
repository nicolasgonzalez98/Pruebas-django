# Generated by Django 4.0.2 on 2023-01-21 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_profesor_alter_curso_inscriptos_alter_curso_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='profesor_id',
            new_name='profesor',
        ),
    ]
