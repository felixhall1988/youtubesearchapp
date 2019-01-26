from __future__ import unicode_literals
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from videoapp import views


urlpatterns = [

    url(r'^channel/(?P<user>.+)/$', views.channel, name='channel'),
    url(r'^admin/', admin.site.urls),
]