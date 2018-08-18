from django.shortcuts import render

from .models import Categories

# Create your views here.
def category_list(request):
	data = Categories.objects.all()
	context = {
		"cate_page" : "AISLES",
		"qs" : data
	}
	return render (request, "category/categories.html", context)