from django.shortcuts import render

from .models import Categories
from products.models import Product

# Create your views here.
def category_list(request):
	data = Categories.objects.all()
	context = {
		"cate_page" : "ISLES",
		"qs" : data
	}
	return render (request, "category/categories.html", context)

