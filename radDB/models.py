from django.contrib.gis.db import models



class ARObject(models.Model):
	timeCreated = models.DateTimeField(auto_now_add=True)
	owner = models.TextField()
	description = models.TextField()
	location = models.PointField()
	asset = models.FileField(null=True)		
	
	class Meta:
		ordering = ('timeCreated',)
