# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import budgetbutler.utils


class Migration(migrations.Migration):

    dependencies = [
        ('budgetbutler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='budgetbutler.Category', null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=budgetbutler.utils.current_date, verbose_name='Date'),
        ),
    ]
