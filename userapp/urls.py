from django.conf.urls import patterns, url

from userapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='userapp'),
)