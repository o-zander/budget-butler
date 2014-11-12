from __future__ import unicode_literals

from django.conf import settings
from django import template

register = template.Library()

CURRENCY = settings.CURRENCY


@register.filter
def currency(value):
    return '{value:.2f} {currency}'.format(value=value, currency=CURRENCY)


@register.filter
def amount_class(value, typ):
    if value == 0:
        return 'amount'
    return 'amount %s' % ('positiv' if (value < 0 if typ == 'expense' else value > 0) else 'negativ')


