# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0007_pendidikan_myfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendidikan',
            name='formal',
        ),
        migrations.RemoveField(
            model_name='pendidikan',
            name='informal',
        ),
        migrations.AlterField(
            model_name='pendidikan',
            name='myfield',
            field=models.CharField(max_length=256, null=True, choices=[(b'formal', b'formal'), (b'informal', b'informal')]),
        ),
    ]
