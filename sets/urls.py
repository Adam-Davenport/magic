from django.conf.urls import url
from sets import views

urlpatterns = [
    url(r'^$', views.Index_View, name='index'),
]