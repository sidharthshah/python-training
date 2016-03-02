from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=255)
	mobile = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name
