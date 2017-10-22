# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='goods_sales',
            new_name='good_sales',
        ),
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='goods_status',
            new_name='good_status',
        ),
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='goods_unit',
            new_name='good_unit',
        ),
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='goods_visits',
            new_name='good_visits',
        ),
    ]
