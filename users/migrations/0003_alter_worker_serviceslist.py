# Generated by Django 5.0.2 on 2024-02-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_caseslist_service_servicelist_task_worker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='servicesList',
            field=models.ManyToManyField(blank=True, related_name='workers', to='users.servicelist'),
        ),
    ]