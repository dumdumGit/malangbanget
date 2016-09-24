# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0003_auto_20151226_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='nana_hotel',
            new_name='nama_hotel',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='nm_travel',
            new_name='nama_travel',
        ),
    ]
