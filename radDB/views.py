from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from radDB.models import ARObject
from radDB.serializers import ARObjectSerializer

@csrf_exempt
def ar_object_list(request):
	if request.method == 'GET':
		arObjects = ARObject.objects.all()
		serializer = ARObjectSerializer(arObjects, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ARObjectSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

def ar_object_detail(request, pk):
	try:
		arObject = ARObject.objects.get(pk=pk)
	except ARObject.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ARObjectSerializer(arObject)
		return JsonResponse(serializer.data)
	
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ARObjectSerializer(arObject, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		arObject.delete()
		return HttpResponse(status=204)	
