# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0004_auto_20151226_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(null=True, upload_to=b'hotel'),
        ),
        migrations.AddField(
            model_name='travel',
            name='image',
            field=models.ImageField(null=True, upload_to=b'travel'),
        ),
    ]
