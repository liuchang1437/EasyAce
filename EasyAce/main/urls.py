from django.conf.urls import url
from . import views
app_name = 'main'

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^$', views.index),
    url(r'^tutors/',views.view_tutor,name='view_tutor'),
    url(r'information/(?P<id>[0-9]+)',views.information,name='information'),
    url(r'edit/$',views.edit,name='edit'),
	url(r'choose_tutor/$',views.choose_tutor,name='choose_tutor'),
	url(r'edit_student/',views.edit_student,name='edit_student'),
	url(r'edit_tutor/',views.edit_tutor,name='edit_tutor'),
    url(r'feedback/record_(?P<record_id>[0-9]+)',views.feedback,name='feedback')
]