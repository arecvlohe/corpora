# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0027_person_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_email',
            field=models.EmailField(blank=True, help_text="This is a placeholder for users that don't sign up.", max_length=254, null=True),
        ),
    ]