# Generated by Django 5.1.1 on 2024-09-29 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('In progress', 'In progress'), ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Done', 'Done')], default='New', max_length=20)),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='task_manager.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('In progress', 'In progress'), ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Done', 'Done')], default='New', max_length=20)),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='task_manager.task')),
            ],
        ),
    ]
