from django.conf.urls import url
from cards import views

urlpatterns = [
    url(r'^set/$', views.Set_View, name='set'),
    # url(r'^$', views.Booster_View, name='booster'),
    url(r'^boosterbattle', views.Booster_View, name='booster'),
]