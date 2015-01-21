# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=250, verbose_name=b'value')),
                ('pos', models.SmallIntegerField(default=b'0', verbose_name=b'position')),
            ],
            options={
                'ordering': ['pos'],
                'verbose_name': 'answer',
                'verbose_name_plural': 'answers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'question')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'date')),
                ('is_published', models.BooleanField(default=True, verbose_name=b'is published')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'poll',
                'verbose_name_plural': 'polls',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(verbose_name=b"user's IP")),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(verbose_name=b'voted item', to='poll.Item')),
                ('poll', models.ForeignKey(verbose_name=b'poll', to='poll.Poll')),
                ('user', models.ForeignKey(verbose_name=b'user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='poll',
            field=models.ForeignKey(to='poll.Poll'),
            preserve_default=True,
        ),
    ]
