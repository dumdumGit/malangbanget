# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0008_auto_20151228_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendidikan',
            name='myfield',
        ),
        migrations.AddField(
            model_name='pendidikan',
            name='jenis',
            field=models.CharField(max_length=35, null=True, choices=[(b'formal', b'formal'), (b'informal', b'informal')]),
        ),
        migrations.AddField(
            model_name='pendidikan',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
