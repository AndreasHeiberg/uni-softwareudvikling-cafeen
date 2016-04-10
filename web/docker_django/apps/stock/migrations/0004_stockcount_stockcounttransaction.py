# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0003_auto_20160409_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockCount',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='StockCountTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('count_id', models.ForeignKey(null=True, to='stock.StockCount')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='stock.Product')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
