# Generated by Django 3.1.5 on 2021-01-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bg_eveonline_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eveuser',
            name='alliance_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eveuser',
            name='character_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eveuser',
            name='corporation_id',
            field=models.IntegerField(null=True),
        ),
    ]
