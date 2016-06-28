from django.conf.urls import url
from . import views
app_name = 'myAuth'

urlpatterns = [
  url(r'^login/$',views.login, name='login'),
  url(r'^logout/$',views.logout, name='logout'),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^signup/tutor/(?P<id>[0-9]+)',views.signup_tutor,name='signup_tutor'),
  url(r'^signup/student/(?P<id>[0-9]+)',views.signup_student,name='signup_student')
]