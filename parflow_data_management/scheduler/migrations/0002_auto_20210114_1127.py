# Generated by Django 3.0.10 on 2021-01-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='large_file_chunk_size',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='large_file_threshold',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
