# Generated by Django 2.1.2 on 2018-10-30 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0009_persona_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='estado',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
