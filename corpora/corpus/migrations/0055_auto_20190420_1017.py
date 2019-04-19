# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-19 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0050_auto_20181204_1032'),
        ('corpus', '0054_auto_20190419_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentenceQualityControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.PositiveIntegerField(default=0, help_text='Indicates the object is good. Can be any interger >= 0.')),
                ('bad', models.PositiveIntegerField(default=0, help_text='Indicates the object is bad. Can be any interger >= 0.')),
                ('approved', models.BooleanField(default=False, help_text='Approved indicates that the object is suitable for use.')),
                ('trash', models.BooleanField(default=False, help_text='Flag for deletion.')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, help_text='Field for providing extra information about a review.', null=True)),
                ('machine', models.BooleanField(default=False, help_text='Boolean to indicate if a machine made the review.')),
            ],
        ),
        migrations.RemoveIndex(
            model_name='recordingqualitycontrol',
            name='corpus_qual_object__11b3d6_idx',
        ),
        migrations.RemoveIndex(
            model_name='recordingqualitycontrol',
            name='corpus_qual_delete_40327a_idx',
        ),
        migrations.RemoveIndex(
            model_name='recordingqualitycontrol',
            name='corpus_qual_approve_cf686b_idx',
        ),
        migrations.RemoveIndex(
            model_name='recordingqualitycontrol',
            name='corpus_qual_good_dc134e_idx',
        ),
        migrations.RemoveIndex(
            model_name='recordingqualitycontrol',
            name='corpus_qual_bad_9c4980_idx',
        ),
        migrations.RenameField(
            model_name='recordingqualitycontrol',
            old_name='delete',
            new_name='trash',
        ),
        migrations.AddField(
            model_name='recordingqualitycontrol',
            name='recording',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quality_control', to='corpus.Recording'),
        ),
        migrations.AddIndex(
            model_name='recordingqualitycontrol',
            index=models.Index(fields=['trash'], name='corpus_reco_trash_21236a_idx'),
        ),
        migrations.AddIndex(
            model_name='recordingqualitycontrol',
            index=models.Index(fields=['approved'], name='corpus_reco_approve_5516cb_idx'),
        ),
        migrations.AddIndex(
            model_name='recordingqualitycontrol',
            index=models.Index(fields=['good'], name='corpus_reco_good_2b9d2a_idx'),
        ),
        migrations.AddIndex(
            model_name='recordingqualitycontrol',
            index=models.Index(fields=['bad'], name='corpus_reco_bad_3f2a30_idx'),
        ),
        migrations.AddField(
            model_name='sentencequalitycontrol',
            name='approved_by',
            field=models.ForeignKey(blank=True, help_text='User that approved the object. Should be a user ID.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sentencequalitycontrol',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
        migrations.AddField(
            model_name='sentencequalitycontrol',
            name='sentence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quality_control', to='corpus.Sentence'),
        ),
        migrations.AddField(
            model_name='sentencequalitycontrol',
            name='source',
            field=models.ForeignKey(blank=True, help_text='Used to identify machines.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='corpus.Source'),
        ),
        migrations.AlterUniqueTogether(
            name='sentencequalitycontrol',
            unique_together=set([('sentence', 'person')]),
        ),
    ]