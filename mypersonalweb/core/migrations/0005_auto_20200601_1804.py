# Generated by Django 3.0.3 on 2020-06-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200601_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfdocument',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]