from django.conf.urls import url
from . import views
app_name = 'main'

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^$', views.index),
    url(r'^tutors/',views.view_tutor),
    url(r'information/(?P<id>[0-9]+)',views.information,name='information'),
    url(r'modify/(?P<id>[0-9]+)',views.modification,name='modification'),
]