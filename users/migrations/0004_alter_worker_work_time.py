# Generated by Django 5.0.2 on 2024-02-10 16:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_worker_serviceslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='work_time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), null=True, size=None),
        ),
    ]
