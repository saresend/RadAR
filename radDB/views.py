from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from radDB.models import ARObject
from radDB.serializers import ARObjectSerializer

class ARObjectList(APIView):
	def get(self, request, format=None):
		 arObjects = ARObject.objects.all()
                 serializer = ARObjectSerializer(arObjects, many=True)
                 return Response(serializer.data)		

	def post(self, request, format=None):
		serializer = ARObjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ARObjectDetail(APIView):
	def get_object(self, pk):
		try:
			arObject = ARObject.objects.get(pk=pk)
		except ARObject.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk, format=None):
		arObject = self.get_object(pk)
		serializer = ARObjectSerializer(arObject)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		arObject = self.get_object(pk)
		serializer = ARObjectSerializer(arObject, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		arObject = self.get_object(pk)
		arObject.delete()
		return Response(status=HTTP_204_NO_CONTENT)	
