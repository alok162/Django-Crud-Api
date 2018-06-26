from django.conf.urls import url
from gateway_app import views

urlpatterns = [
    url(r'^gateway/$', views.Gateway_Post.as_view()),
    url(r'gateway_patch/(?P<pk>\d+)$', views.Gateway_Update.as_view()),
    url(r'^gateway_detail/(?P<pk>[0-9]+)/$', views.Gateway_Detail.as_view()),
    url(r'^route_mapping/$', views.Route_Mapping.as_view()),
    url(r'^route_mapping_detail/(?P<pk>[0-9]+)/$', views.Route_Mapping_Detail.as_view()),
    url(r'^get_prefix/(?P<pk>[0-9]+)/$', views.GetPrefix.as_view()),
]
