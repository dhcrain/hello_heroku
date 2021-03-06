# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-10 22:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hash_id', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_click', models.DateTimeField()),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='short_app.Bookmark')),
            ],
            options={
                'ordering': ['-time_click'],
            },
        ),
    ]
