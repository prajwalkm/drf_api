   apicust is project name and POST is name of app
   
    
    
   Url to access API'S: 


    url(r'^user/create/$', UserCreateView.as_view(), name='create'),
    url(r'^user/list/$', UserListView.as_view(), name='list'),
    url(r'^user/(?P<pk>\d+)/detail/$', UserDetailView.as_view(), name='detail'),
    url(r'^user/(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='update'),
    url(r'^user/(?P<pk>\d+)/delete/$', UserDeleteView.as_view(), name='delete'),




New URLS:

    url(r'^$', home, name='home'),
    url(r'^register/$',UserCreateAPIView.as_view() , name='register'),
    url(r'^welcome/$',welcome , name='welcome'),
    url(r'^user/edit/(?P<pk>\d+)/$', ProfileDetail.as_view(), name='Profile-Detail'),

