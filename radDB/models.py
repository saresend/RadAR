from django.db import models



class ARObject(models.Model):
	timeCreated = models.DateTimeField(auto_now_add=True)
	owner = models.TextField()
	description = models.TextField()
	location = models.PointField()
	asset = models.FileField(upload_to='media')		
	
	class Meta:
		ordering = ('timeCreated')
