# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0006_auto_20151228_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendidikan',
            name='myfield',
            field=models.CharField(max_length=256, null=True, choices=[(b'green', b'green'), (b'red', b'red')]),
        ),
    ]
