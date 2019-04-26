# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 03:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0055_auto_20190420_1549'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0050_auto_20181204_1032'),
        ('transcription', '0022_transcription_word_error_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranscriptionQualityControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.PositiveIntegerField(default=0, help_text='Indicates the object is good. Can be any interger >= 0.')),
                ('bad', models.PositiveIntegerField(default=0, help_text='Indicates the object is bad. Can be any interger >= 0.')),
                ('approved', models.BooleanField(default=False, help_text='Approved indicates that the object is suitable for use.')),
                ('trash', models.BooleanField(default=False, help_text='Flag for deletion.')),
                ('star', models.PositiveIntegerField(default=0, help_text='Stars are to indicate an object is amazing. This is a positive        interger field so we can, for example, do a 5 star rating system.')),
                ('follow_up', models.BooleanField(default=False, help_text='Flag an item for follow up later.')),
                ('noise', models.BooleanField(default=False, help_text='Check if an item has noise but is still intelligible.')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, help_text='Field for providing extra information about a review.', null=True)),
                ('machine', models.BooleanField(default=False, help_text='Boolean to indicate if a machine made the review.')),
                ('approved_by', models.ForeignKey(blank=True, help_text='User that approved the object. Should be a user ID.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(blank=True, help_text="ID of person associated with this QualityControl object.        For Token Authenticated API calls, passing the string 'self' instead        of an Integer will associate the person of the Token with this QC         object.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Person')),
                ('source', models.ForeignKey(blank=True, help_text='Used to identify machines.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='corpus.Source')),
                ('transcription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transcription.Transcription')),
            ],
        ),
        migrations.AddIndex(
            model_name='transcriptionqualitycontrol',
            index=models.Index(fields=['trash'], name='transcripti_trash_a9c676_idx'),
        ),
        migrations.AddIndex(
            model_name='transcriptionqualitycontrol',
            index=models.Index(fields=['approved'], name='transcripti_approve_71c2ae_idx'),
        ),
        migrations.AddIndex(
            model_name='transcriptionqualitycontrol',
            index=models.Index(fields=['good'], name='transcripti_good_7fa017_idx'),
        ),
        migrations.AddIndex(
            model_name='transcriptionqualitycontrol',
            index=models.Index(fields=['bad'], name='transcripti_bad_3efbcd_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='transcriptionqualitycontrol',
            unique_together=set([('transcription', 'person')]),
        ),
    ]