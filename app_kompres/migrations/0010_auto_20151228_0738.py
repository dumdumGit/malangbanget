# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0009_auto_20151228_0731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pendidikan',
            old_name='jenis',
            new_name='kategori',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='kategori_hotel',
        ),
        migrations.AddField(
            model_name='hotel',
            name='kategori',
            field=models.CharField(max_length=35, null=True, choices=[(b'satu', b'satu'), (b'dua', b'dua'), (b'tiga', b'tiga'), (b'empat', b'empat'), (b'lima', b'lima')]),
        ),
    ]
