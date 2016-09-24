# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='kategori_htl',
            new_name='kategori_hotel',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='link_htl',
            new_name='link_hotel',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='nm_htl',
            new_name='nana_hotel',
        ),
        migrations.AddField(
            model_name='travel',
            name='info',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
