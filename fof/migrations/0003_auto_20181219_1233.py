# Generated by Django 2.1.4 on 2018-12-19 14:33

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('fof', '0002_auto_20181219_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fofalgorithm',
            old_name='command',
            new_name='commandFoF',
        ),
        migrations.RenameField(
            model_name='fofalgorithm',
            old_name='desc',
            new_name='descFoF',
        ),
        migrations.RenameField(
            model_name='fofalgorithm',
            old_name='idAlg',
            new_name='idFoF',
        ),
        migrations.RenameField(
            model_name='fofalgorithm',
            old_name='nameAlg',
            new_name='nameFoF',
        ),
    ]