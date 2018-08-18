from django.db import models


class Categories(models.Model):
	cate_name = models.CharField(max_length=120)
	description = models.TextField()

	def __str__(self):
		return self.cate_name
