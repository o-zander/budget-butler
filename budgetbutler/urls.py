from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexView, MonthDetailView, ExpenseListView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', MonthDetailView.as_view(), name='month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', ExpenseListView.as_view(), name='day'),
    url(r'^admin/', include(admin.site.urls)),
)
