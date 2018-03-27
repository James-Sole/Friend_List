from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^friends$', views.friends),
    url(r'^user/(?P<id>\d+)$', views.userId),
    url(r'^friend/add/(?P<id>\d+)$', views.Add),
    url(r'^friend/remove/(?P<id>\d+)$', views.Remove),
]
