# Generated by Django 5.0.2 on 2024-02-10 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_worker_serviceslist_delete_servicelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=30)),
                ('like', models.CharField(max_length=100)),
            ],
        ),
    ]
