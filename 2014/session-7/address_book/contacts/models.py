from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=255)
	mobile = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name

class Address(models.Model):
	street_address = models.CharField(max_length=255)
	building = models.CharField(max_length=255)
	pincode = models.CharField(max_length=6)

 	def __unicode__(self):
		return self.street_address
