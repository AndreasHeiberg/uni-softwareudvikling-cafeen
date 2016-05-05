# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='StockCountTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock', models.IntegerField()),
                ('count', models.ForeignKey(to='stock.StockCount', null=True)),
                ('product', models.ForeignKey(null=True, to='stock.Product', on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
