# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='answer',
            field=models.CharField(max_length=150, null=True, verbose_name=b'answer', blank=True),
            preserve_default=True,
        ),
    ]
