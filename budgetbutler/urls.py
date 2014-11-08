from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import RedirectToToday, ExpenseListView, ExpenseAddView

expenses = patterns(
    '',
    url(r'^$', RedirectToToday.as_view(), name='overview'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', ExpenseListView.as_view(), name='daily'),
    url(r'^add/$', ExpenseAddView.as_view(), name='add'),
)

urlpatterns = patterns(
    '',
    url(r'^$', RedirectToToday.as_view(), name='index'),
    url(r'^expenses/', include(expenses, namespace='expenses')),
    url(r'^admin/', include(admin.site.urls)),
)
