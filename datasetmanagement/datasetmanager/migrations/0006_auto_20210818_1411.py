# Generated by Django 3.2.6 on 2021-08-18 07:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasetmanager', '0005_auto_20210817_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='uploader',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='datasetmanager.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='file',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip'])]),
        ),
    ]