# Generated by Django 3.0.10 on 2021-02-17 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20210217_1638'),
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetstore',
            name='cluster',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Cluster'),
        ),
    ]
