# Generated by Django 3.2.8 on 2021-12-04 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_auto_20211204_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pdtriplenew',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='prescribercredential',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='prescriberspecialty',
            options={'managed': False},
        ),
        migrations.AlterField(
            model_name='pdprescriber',
            name='state',
            field=models.ForeignKey(default='AL', on_delete=django.db.models.deletion.DO_NOTHING, to='WebApp.pdstatedata'),
        ),
    ]
