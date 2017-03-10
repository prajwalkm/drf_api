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

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from post.views import UserCreateView,UserListView,UserDetailView,UserUpdateView,UserDeleteView,home,ProfileDetail
from post.views import UserCreateAPIView,welcome,home


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^register/$',UserCreateAPIView.as_view() , name='register'),
    url(r'^welcome/$',welcome , name='welcome'),
    url(r'^user/edit/(?P<pk>\d+)/$', ProfileDetail.as_view(), name='Profile-Detail'),


    url(r'^user/create/$', UserCreateView.as_view(), name='create'),
    url(r'^user/list/$', UserListView.as_view(), name='list'),
    url(r'^user/(?P<pk>\d+)/detail/$', UserDetailView.as_view(), name='detail'),
    url(r'^user/update/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='update'),
    url(r'^user/(?P<pk>\d+)/delete/$', UserDeleteView.as_view(), name='delete'),
    url(r'^accounts/', include('registration.backends.default.urls')),


]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
