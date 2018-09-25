from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^gallery/$', views.gallery),
    url(r'^diary/$', views.diary),
    url(r'^about/$', views.about),
    url(r'^message/$', views.message),
    url(r'^info/$', views.info),
    url(r'^infopic/$', views.infopic),
    #url(r'^/$', views., name=''),
    url(r'^test/$', views.test, name='test'),
]