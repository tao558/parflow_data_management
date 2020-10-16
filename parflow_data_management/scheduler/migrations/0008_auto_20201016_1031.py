# Generated by Django 3.1.2 on 2020-10-16 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20201016_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptualmodel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conceptualmodels', to='scheduler.project'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meshs', to='scheduler.project'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metadatas', to='scheduler.project'),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simulations', to='scheduler.project'),
        ),
    ]