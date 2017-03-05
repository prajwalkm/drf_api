"""apicust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from post.views import UserCreateView,UserListView,UserDetailView,UserUpdateView,UserDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/create/$', UserCreateView.as_view(), name='create'),
    url(r'^user/list/$', UserListView.as_view(), name='list'),
    url(r'^user/(?P<pk>\d+)/detail/$', UserDetailView.as_view(), name='detail'),
    url(r'^user/(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='update'),
    url(r'^user/(?P<pk>\d+)/delete/$', UserDeleteView.as_view(), name='delete'),


]
