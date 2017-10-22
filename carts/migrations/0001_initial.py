# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_recordbrowse'),
        ('goods', '0003_auto_20171020_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_del', models.BooleanField(default=False)),
                ('cart_amount', models.IntegerField()),
                ('cart_goods', models.ForeignKey(to='goods.GoodsInfo')),
                ('cart_user', models.ForeignKey(to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
