# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import current_date

class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Expense(models.Model):
    date = models.DateField(_('Date'), default=current_date)
    amount = models.DecimalField(_('Amount'), decimal_places=2, max_digits=8)
    description = models.CharField(_('Description'), max_length=100)
    category = models.ForeignKey(Category, verbose_name=_('Category'))

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')
        ordering = ('-date',)

    def __unicode__(self):
        return '{0} ({1}): {2}€'.format(self.description, self.date, self.amount)