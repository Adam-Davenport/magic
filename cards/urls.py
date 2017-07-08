from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from cards import views

urlpatterns = [
    url(r'^$', views.Index_View, name='index'),
    url(r'^set/$', views.Set_View, name='set'),
    url(r'^boosters/$', views.Booster_View, name='boosters'),
    url(r'^battles/$', views.Battle_List_View, name='battles'),
    url(r'^battles/(?P<pk>\d)/$', views.Battle_View, name='battle_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
