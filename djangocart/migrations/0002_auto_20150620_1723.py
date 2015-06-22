# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='has_voucher',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='voucher_code',
            field=models.CharField(null=True, max_length=250, blank=True),
        ),
    ]
