# Generated by Django 2.1.2 on 2018-10-30 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_persona_contrasenia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='foto',
            field=models.ImageField(upload_to='fotos/'),
        ),
    ]
