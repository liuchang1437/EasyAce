"""EasyAce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.conf.urls import url, include
from django.contrib import admin
from myView import views as my_view
from main import views as main_view

urlpatterns = [
    url(r'^photos/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'photos'}),
    url(r'^about/', my_view.about),
    url(r'^auth/', include('myAuth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', my_view.contact),
    url(r'^for_student/', my_view.for_student),
    url(r'^for_tutor/', my_view.for_tutor),
    url(r'^', include('main.urls')),
]
