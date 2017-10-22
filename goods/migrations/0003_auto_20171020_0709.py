# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20171019_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_del', models.BooleanField(default=False)),
                ('ad_name', models.CharField(max_length=30)),
                ('ad_image', models.ImageField(upload_to='ad')),
                ('ad_link', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='GoodsInfoManager',
        ),
    ]
