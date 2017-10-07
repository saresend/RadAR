from django.db import models



class ARObject(models.Model):
	timeCreated = models.DateTimeField(auto_now_add=True)
	owner = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	location = models.CharField(max_length=1000)
	asset = models.FileField(upload_to='media', null=True)		
	
	class Meta:
		ordering = ('timeCreated',)
