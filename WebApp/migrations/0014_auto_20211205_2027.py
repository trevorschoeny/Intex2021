# Generated by Django 3.2.8 on 2021-12-05 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0013_auto_20211205_2011'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pdprescriberspecialtieslink',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='pdprescriberspecialtieslink',
            name='pdprescriber',
        ),
        migrations.RemoveField(
            model_name='pdprescriberspecialtieslink',
            name='pdspecialty',
        ),
        migrations.RemoveField(
            model_name='pdprescriber',
            name='specialties',
        ),
        migrations.DeleteModel(
            name='PdPrescriberSpecialties',
        ),
        migrations.DeleteModel(
            name='PdPrescriberSpecialtiesLink',
        ),
    ]
