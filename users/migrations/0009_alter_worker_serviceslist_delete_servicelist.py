# Generated by Django 5.0.2 on 2024-02-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_delete_workerlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='servicesList',
            field=models.ManyToManyField(blank=True, related_name='workers', to='users.service'),
        ),
        migrations.DeleteModel(
            name='ServiceList',
        ),
    ]