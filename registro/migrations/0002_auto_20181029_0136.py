# Generated by Django 2.1.2 on 2018-10-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='ciudad',
            new_name='comuna',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='fechaNac',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='tipoViv',
            new_name='vivienda',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='rut',
        ),
        migrations.AddField(
            model_name='persona',
            name='run',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
