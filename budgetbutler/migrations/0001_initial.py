# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('amount', models.DecimalField(verbose_name='Amount', max_digits=8, decimal_places=2)),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('category', models.ForeignKey(verbose_name='Category', to='budgetbutler.Category')),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
            bases=(models.Model,),
        ),
    ]
