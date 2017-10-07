from rest_framework import serializers
from radDB.models import ARObject

class ARObjectSerializer(serializers.Serializer):
	timeCreated = serializers.DateTimeField()
	owner = serializers.CharField()	
	description = serializers.CharField()
	location = serializers.CharField()
	asset = serializers.FileField(allow_null=True)

	def create(self, validated_data):
		return ARObject.objects.create(**validated_data)
	

	def update(self, instance, validated_data):
		instance.description = validated_data.get('description', instance.description)
		instance.location = validated_data.get('location', instance.location)
		instance.asset = validated_data.get('asset', instance.asset)
		instance.save()
		return instance
