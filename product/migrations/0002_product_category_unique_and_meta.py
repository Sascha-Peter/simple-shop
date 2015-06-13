# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'product categories'},
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
