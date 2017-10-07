from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class ARObject
	timeCreated = models.DateTimeField(auto_now_add=True)
	owner = models.TextField()
	description = models.TextField()
	location = models.PointField()
	asset = models.FileField(upload_to='media')		
	
	class Meta:
		ordering = ('timeCreated')
