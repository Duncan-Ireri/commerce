import random
import os
# from django.forms import ModelChoiceField
from django.db import models
from categories.models import Categories

def get_filext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def uploaded_path(instance, filename):
	new_filename = random.randint(1, 9989239892398998923899)
	name, ext = get_filext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class ProductManager(models.Manager):
	def get_by_id(self, id):
		# return self.get_queryset().filter(id=id)
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

class Product(models.Model):
	title       = models.CharField(max_length=120)
	# slug  		= models.SlugField(blank=True)
	description = models.TextField()
	price 		= models.DecimalField(decimal_places=2, max_digits=20, default=300.00)
	categ 		= models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
	image 		= models.ImageField(upload_to=uploaded_path, null=True, blank=True)
	timestamp	= models.DateField(auto_now_add=True)

	objects = ProductManager()

	def __str__(self):
		return self.title
