# Generated by Django 3.1.5 on 2021-01-10 01:36

import apps.bg_eveonline_sde.utils
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dgmTypeAttributes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeattributes',
            name='valueFloat',
            field=apps.bg_eveonline_sde.utils.CustomFloatField(null=True),
        ),
    ]
