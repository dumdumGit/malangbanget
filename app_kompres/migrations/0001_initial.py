# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True)),
                ('isi', ckeditor.fields.RichTextField(null=True)),
                ('image_post', models.ImageField(null=True, upload_to=b'post_artikel')),
                ('image_height', models.PositiveIntegerField(default=b'190', null=True, editable=False)),
                ('image_width', models.PositiveIntegerField(default=b'350', null=True, editable=False)),
                ('tgl_buat', models.DateTimeField(auto_now=True, null=True)),
                ('link', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('organizer', models.CharField(max_length=30)),
                ('venue', models.CharField(max_length=30)),
                ('about', ckeditor.fields.RichTextField(blank=True)),
                ('poster', models.ImageField(upload_to=b'poster')),
                ('date_begin', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['date_begin'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gambar', models.ImageField(upload_to=b'poster')),
                ('tanggal_upload', models.DateTimeField(auto_now=True)),
                ('about', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm_htl', models.CharField(max_length=30)),
                ('no_tlp', models.IntegerField()),
                ('tgl_pub', models.DateTimeField(auto_now=True)),
                ('link_htl', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('kategori_htl', models.CharField(max_length=20)),
                ('info', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='kuliner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', ckeditor.fields.RichTextField(null=True)),
                ('nama_kuliner', models.CharField(max_length=60, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('image_kuliner', models.ImageField(null=True, upload_to=b'kuliner')),
                ('tempat', models.CharField(max_length=255, null=True)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63, null=True)),
            ],
            options={
                'ordering': ['last_modified'],
            },
        ),
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm_trvl', models.CharField(max_length=30)),
                ('no_tlp', models.IntegerField()),
                ('tgl_pub', models.DateTimeField(auto_now=True)),
                ('link_trvl', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='wisata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', ckeditor.fields.RichTextField(null=True)),
                ('title', models.CharField(max_length=60, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('kategori_wisata', models.CharField(max_length=25, null=True)),
                ('image', models.ImageField(null=True, upload_to=b'kotwis')),
                ('tempat', models.CharField(max_length=255, null=True)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63, null=True)),
            ],
            options={
                'ordering': ['last_modified'],
            },
        ),
    ]
