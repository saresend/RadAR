from django.conf.urls import url
from radDB import views

urlpatterns = [
	url(r'^radDB/$', views.ar_object_list),
	url(r'^radDB/(?P<pk>[0-9]+)/$', views.ar_object_detail),
]
