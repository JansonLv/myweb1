# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20171020_0709'),
        ('users', '0002_user_user_recv'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordBrowse',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_del', models.BooleanField(default=False)),
                ('browse_good', models.ForeignKey(to='goods.GoodsInfo')),
                ('browse_user', models.ForeignKey(to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
