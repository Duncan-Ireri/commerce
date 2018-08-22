from django.db import models

# Create your models here.
class SuperName(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class SuperSize(models.Model):
	size = models.CharField(max_length=120)

	def __str__ (self):
		return self.size

class SuperSub(models.Model):
	superstore = models.ForeignKey(SuperName, on_delete=models.CASCADE, null=True)
	substore = models.CharField(max_length=120)
	lat = models.DecimalField(max_digits=12, decimal_places=9)
	lon = models.DecimalField(max_digits=12, decimal_places=9)
	location_name = models.CharField(max_length=120)
	size = models.ForeignKey(SuperSize, on_delete=models.CASCADE, null=True)

	def __str__ (self):
		return self.substore
