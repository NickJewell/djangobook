from django.conf.urls import patterns, url
from mysite import views

urlpatterns = patterns('',
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
)