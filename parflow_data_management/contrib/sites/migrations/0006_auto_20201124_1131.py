# Generated by Django 3.1.3 on 2020-11-24 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_auto_20201023_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['domain'], 'verbose_name': 'site', 'verbose_name_plural': 'sites'},
        ),
    ]
