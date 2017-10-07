from django.shortcuts import render
from rest_framework import generics
from radDB.models import ARObject
from radDB.serializers import ARObjectSerializer
# Create your views here.



class ARObjectList(generics.ListCreateAPIView):
    queryset = ARObject.objects.all()
    serializer_class = ARObjectSerializer



class ARObjectUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ARObject.objects.all()
    serializer_class = ARObjectSerializer
