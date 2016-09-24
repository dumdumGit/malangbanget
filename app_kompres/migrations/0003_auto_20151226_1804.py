# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0002_auto_20151226_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel',
            old_name='link_trvl',
            new_name='link_travel',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='nm_trvl',
            new_name='nm_travel',
        ),
    ]
