import calendar
import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone


def current_date():
    return timezone.now().date()


def get_date_url(date=None, view=None):
    date, view = date or current_date(), view or 'day'
    year, month, day = date.strftime('%Y-%m-%d').split('-')
    kwargs = dict(zip(('year', 'month', 'day'), (year, month, day)))
    return reverse(view, kwargs=kwargs)


def get_months(year):
    return [
        datetime.date(year, month, 1)
        for month in range(1, 13)
    ]


def get_month_range(date):
    return calendar.monthrange(date.year, date.month)


def get_days(year, month):
    monthdatescalendar = calendar.Calendar().monthdatescalendar(year, month)

    def week_with_days():
        for week in monthdatescalendar:
            firstday, = week[:1]
            weekofyear, weekday = firstday.isocalendar()[1:]
            yield [weekofyear, week]

    return list(week_with_days())