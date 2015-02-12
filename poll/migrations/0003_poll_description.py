# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_poll_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
            preserve_default=True,
        ),
    ]
