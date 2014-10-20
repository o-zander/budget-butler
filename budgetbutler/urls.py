from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexView, ExpenseView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^expenses/$', ExpenseView.as_view(), name='expenses'),
    url(r'^admin/', include(admin.site.urls)),
)
