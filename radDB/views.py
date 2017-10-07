from django.shortcuts import render
from rest_framework import generics
from radDB.models import ARObject
from radDB.serializers import ARObjectSerializer
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
# Create your views here.



class ARObjectList(generics.ListCreateAPIView):

    def get_queryset(self):
        lat = self.request.GET.get('lat') or None
        lng = self.request.GET.get('lng') or None
        if lat == None or lng == None:
            return ARObject.objects.all()
        pnt = GEOSGeometry('POINT(' + str(lat) + ' ' + str(lng) + ')', srid=4326)
        queryset = ARObject.objects.filter(location__distance_lte=(pnt, 1000))
        return queryset
        
    serializer_class = ARObjectSerializer



class ARObjectUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ARObject.objects.all()
    serializer_class = ARObjectSerializer
