# Generated by Django 3.2.8 on 2021-12-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0011_auto_20211205_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdprescriber',
            name='specialties',
            field=models.ManyToManyField(through='WebApp.PdPrescriberSpecialties', to='WebApp.PdSpecialty'),
        ),
    ]
