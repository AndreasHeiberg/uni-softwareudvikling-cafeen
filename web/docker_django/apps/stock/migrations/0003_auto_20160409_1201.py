# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_product_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='productgroup',
            options={'ordering': ['pk']},
        ),
    ]
