# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 16:04
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
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_click', models.DateTimeField(auto_now_add=True)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='short_app.Bookmark')),
            ],
            options={
                'ordering': ['-time_click'],
            },
        ),
        migrations.CreateModel(
            name='Hash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.CharField(max_length=10)),
                ('count', models.IntegerField(default=0)),
                ('bookmark', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='short_app.Bookmark')),
            ],
        ),
    ]