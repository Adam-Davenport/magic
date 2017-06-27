from django.conf.urls import url
from django.conf.urls.static import staic
from django.conf import settings
from cards import views

urlpatterns = [
    url(r'^set/$', views.Set_View, name='set'),
    # url(r'^$', views.Booster_View, name='booster'),
    url(r'^boosterbattle', views.Booster_View, name='booster'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)