# Generated by Django 3.2.6 on 2021-08-19 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasetmanager', '0002_auto_20210819_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='booker',
        ),
        migrations.AddField(
            model_name='dataset',
            name='booker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booker', to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
    ]
