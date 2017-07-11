from django.conf.urls import url
from sets import views

urlpatterns = [
    url(r'^$', views.Index_View, name='index'),
    url(r'^(?P<pk>\w+)/$', views.Details_View, name='details')
]