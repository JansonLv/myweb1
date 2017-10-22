# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_del', models.BooleanField(default=False)),
                ('cag_name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_del', models.BooleanField(default=False)),
                ('good_name', models.CharField(max_length=30)),
                ('good_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('good_image', models.ImageField(upload_to='')),
                ('good_compendium', models.CharField(max_length=100)),
                ('good_details', tinymce.models.HTMLField()),
                ('goods_status', models.BooleanField(default=True)),
                ('goods_unit', models.CharField(max_length=20)),
                ('goods_visits', models.IntegerField(default=0)),
                ('goods_sales', models.IntegerField(default=0)),
                ('goods_cag', models.ForeignKey(to='goods.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsInfoManager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
    ]
