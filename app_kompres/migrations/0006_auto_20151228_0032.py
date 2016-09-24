# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('app_kompres', '0005_auto_20151227_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendidikan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institusi', models.CharField(max_length=80)),
                ('formal', models.BooleanField(default=False)),
                ('informal', models.BooleanField(default=False)),
                ('SD', models.BooleanField(default=False)),
                ('SMP', models.BooleanField(default=False)),
                ('SMA', models.BooleanField(default=False)),
                ('Perguruan_Tinggi', models.BooleanField(default=False)),
                ('cover', models.ImageField(upload_to=b'Pendidikan')),
                ('alamat', models.TextField()),
                ('no_telepon', models.IntegerField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('info', ckeditor.fields.RichTextField()),
                ('tempat', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
            options={
                'ordering': ['last_modified'],
            },
        ),
        migrations.CreateModel(
            name='RumahSakit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_rumahsakit', models.CharField(max_length=50)),
                ('cover', models.ImageField(upload_to=b'RumahSakit')),
                ('alamat', models.TextField()),
                ('no_telepon', models.IntegerField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('info', ckeditor.fields.RichTextField()),
                ('tempat', models.CharField(max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
            options={
                'ordering': ['last_modified'],
            },
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.AddField(
            model_name='hotel',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='tempat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='tempat',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
