

from django.conf.urls import url
from radDB import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^arobject/$', views.ARObjectList.as_view()),
    url(r'^arobject/(?P<pk>[0-9]+)/$', views.ARObjectUpdate.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


