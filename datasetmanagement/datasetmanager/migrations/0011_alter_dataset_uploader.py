# Generated by Django 3.2.6 on 2021-08-18 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasetmanager', '0010_alter_dataset_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
    ]
