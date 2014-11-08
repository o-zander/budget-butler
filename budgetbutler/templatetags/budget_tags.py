from __future__ import unicode_literals

from django.conf import settings
from django import template

register = template.Library()

CURRENCY = settings.CURRENCY


@register.filter
def currency(value):
    return '{value:.2f} {currency}'.format(value=value, currency=CURRENCY)