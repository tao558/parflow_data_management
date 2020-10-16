# Generated by Django 3.1.2 on 2020-10-16 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptualmodel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conceptualmodel', to='scheduler.project'),
        ),
        migrations.AlterField(
            model_name='mesh',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesh', to='scheduler.project'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='scheduler.project'),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simulation', to='scheduler.project'),
        ),
    ]