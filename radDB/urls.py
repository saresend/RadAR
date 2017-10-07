from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from radDB import views

urlpatterns = [
	url(r'^radDB/$', views.ARObjectList.as_view()),
	url(r'^radDB/(?P<pk>[0-9]+)/$', views.ARObjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
