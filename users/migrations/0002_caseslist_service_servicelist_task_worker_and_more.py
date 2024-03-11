# Generated by Django 5.0.2 on 2024-02-10 16:22

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Name', max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_lists', to='users.service')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('dateDedline', models.DateTimeField()),
                ('date', models.DateTimeField()),
                ('cases_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.caseslist')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('work_time', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), size=None)),
                ('servicesList', models.ManyToManyField(related_name='workers', to='users.servicelist')),
            ],
        ),
        migrations.AddField(
            model_name='servicelist',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_lists', to='users.worker'),
        ),
        migrations.CreateModel(
            name='WorkerList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('workers', models.ManyToManyField(related_name='worker_lists', to='users.worker')),
            ],
        ),
    ]
