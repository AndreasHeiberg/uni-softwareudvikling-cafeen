# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cafe.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stockcount_stockcounttransaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('rent_out_product', 'Can rent out a product'),), 'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='product',
            name='price_other',
            field=cafe.utils.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockcount',
            name='price_type',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='stockcounttransaction',
            name='name',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockcounttransaction',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
