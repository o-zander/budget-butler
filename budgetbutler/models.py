# coding=utf-8
from __future__ import unicode_literals

from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import current_date, get_date_url, get_month_range

CURRENCY = settings.CURRENCY


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class BaseExpense(models.Model):
    amount = models.DecimalField(_('Amount'), decimal_places=2, max_digits=8, help_text=CURRENCY)
    description = models.CharField(_('Description'), max_length=100)
    category = models.ForeignKey(Category, verbose_name=_('Category'), blank=True, null=True)

    class Meta:
        abstract = True


class ExpenseQuerySet(models.QuerySet):

    def get_sum_amount(self):
        qs = self.aggregate(sum=models.Sum('amount'))
        return qs.get('sum') or Decimal('0.00')

    def get_budget(self, date):
        first, last = get_month_range(date)
        amount = self.filter(date__lt=date).get_sum_amount() * -1
        return amount / (last + 1 - date.day)


class Expense(BaseExpense):
    date = models.DateField(_('Date'), default=current_date)

    objects = ExpenseQuerySet.as_manager()

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')
        ordering = ('-date',)

    def __unicode__(self):
        return '{0} ({1:%x}): {2:.2f} {3}'.format(self.description, self.date, self.amount, CURRENCY)

    def get_absolute_url(self):
        return get_date_url(date=self.date)