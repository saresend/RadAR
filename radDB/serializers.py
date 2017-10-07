

from rest_framework import serializers
from radDB.models import ARObject

class ARObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARObject 
        fields = ('id', 'timeCreated', 'owner', 'description', 'location', 'asset')

