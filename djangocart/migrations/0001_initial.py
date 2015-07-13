# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('checked_out', models.BooleanField(verbose_name='checked out', default=False)),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'ordering': ('-creation_date',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('unit_price', models.DecimalField(max_digits=18, verbose_name='unit price', decimal_places=2)),
                ('object_id', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(to='djangocart.Cart', verbose_name='cart')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'ordering': ('cart',),
            },
        ),
    ]
