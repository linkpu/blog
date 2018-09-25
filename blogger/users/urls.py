from django.conf.urls import url

from users import views

urlpatterns = [

    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^article/$', views.article),
    url(r'^notic/$', views.notice),
    url(r'^comment/$', views.comment),
    url(r'^category/$', views.category),
    url(r'^flink/$', views.flink),
    url(r'^manage_user/$', views.manage_user),
    url(r'^loginlog/$', views.loginlog),
    url(r'^setting/$', views.setting),
    url(r'^readset/$', views.readset),
    url(r'^add_article/$', views.add_article),
    # url(r'^/$', views.),
    # url(r'^/$', views.),
    # url(r'^/$', views.),
    # url(r'^/$', views.),
]