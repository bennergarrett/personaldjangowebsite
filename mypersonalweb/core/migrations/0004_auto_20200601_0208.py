# Generated by Django 3.0.3 on 2020-06-01 02:08

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200601_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfdocument',
            name='document',
            field=models.FileField(storage=core.models.OverwriteStorage(), upload_to='resume/'),
        ),
    ]