# Generated by Django 2.1.2 on 2018-10-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20181029_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha',
            field=models.CharField(max_length=100),
        ),
    ]
