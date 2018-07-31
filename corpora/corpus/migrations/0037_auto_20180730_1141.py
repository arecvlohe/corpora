# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-29 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0036_auto_20180727_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualitycontrol',
            name='approved',
            field=models.BooleanField(default=False, help_text='Approved indicates that the object is suitable for use.'),
        ),
        migrations.AlterField(
            model_name='qualitycontrol',
            name='approved_by',
            field=models.ForeignKey(blank=True, help_text='User that approved the object. Should be a user ID.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='qualitycontrol',
            name='bad',
            field=models.PositiveIntegerField(default=0, help_text='Indicates the object is bad. Can be any interger >= 0.'),
        ),
        migrations.AlterField(
            model_name='qualitycontrol',
            name='content_type',
            field=models.ForeignKey(help_text='Model to which this QualityControl refers. This should be         the content type ID. Implemented types are Recordings (id=8),        Sentences (id=10), Transcription Segments (id=24).', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='qualitycontrol',
            name='good',
            field=models.PositiveIntegerField(default=0, help_text='Indicates the object is good. Can be any interger >= 0.'),
        ),
        migrations.AlterField(
            model_name='source',
            name='source_url',
            field=models.URLField(blank=True, help_text='URL for the source (e.g. a website or API endpoint).        This field can be None.', null=True),
        ),
    ]