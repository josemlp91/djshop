# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-06 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20161206_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Main image of the product'),
        ),
    ]