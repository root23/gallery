from django.conf.urls import url
from .import views

app_name = 'photos'

urlpatterns = [
    #register
    url(r'^register/$', views.UserFormView.as_view(), name = 'register'),

    #login
    url(r'^login/$', views.LoginFormView.as_view(), name = 'login'),

    #logout
    url(r'^logout/$', views.LogoutView.as_view(), name = 'logout'),

    # /photos/album/123/
    url(r'album/(?P<pk>[0-9]+)/$',views.UpdateAlbum.as_view(), name = 'album-update'),

    # /photos/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.DeleteAlbum.as_view(), name = 'album-delete'),

    # /photos/123/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    # /photos/album/add
    url(r'album/add/$',views.CreateAlbum.as_view(), name = 'album-add'),

    #/photos/add
    url(r'^add/$', views.CreatePhoto.as_view(), name = 'photo-add'),

    #index
    url(r'^page/(\d+)/$', views.albums, name = 'index'),
    url(r'^', views.albums, name = 'index'),

]