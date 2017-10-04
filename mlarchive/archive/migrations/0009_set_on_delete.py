# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-22 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0008_fix_threads_2189'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archive.EmailList'),
        ),
        migrations.AlterField(
            model_name='message',
            name='in_reply_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='archive.Message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archive.Thread'),
        ),
    ]