# Generated by Django 3.2.8 on 2021-12-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_rename_state_pdprescriber_stateid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdprescriber',
            name='specialties',
            field=models.ManyToManyField(to='WebApp.PdSpecialty'),
        ),
    ]
