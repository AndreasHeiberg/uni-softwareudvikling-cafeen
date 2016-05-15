# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('price_rent', models.IntegerField()),
                ('stock', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(null=True, to='stock.ProductGroup', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
