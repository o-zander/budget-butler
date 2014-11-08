from django.core.urlresolvers import reverse
from django.utils import timezone


def current_date():
    return timezone.now().date()


def get_date_url(date=None, view=None):
    date, view = date or current_date(), view or 'expenses:daily'
    year, month, day = date.strftime('%Y-%m-%d').split('-')
    kwargs = dict(zip(('year', 'month', 'day'), (year, month, day)))
    return reverse(view, kwargs=kwargs)