from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from cards import views

urlpatterns = [
    url(r'^set/$', views.Set_View, name='set'),
    url(r'^$', views.Booster_View, name='index'),
    url(r'^boosterbattle', views.Booster_View, name='booster'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)