import random
from django.http import Http404
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
# from .filters import ProductFilter

from .models import Product
from categories.models import Categories

# Create your views here.
def product_list(request):
	queryset = Product.objects.order_by('?')[:5]
	# special = Product.objects.filter(cate_name__icontains ="food")
	context ={
		"hero":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab, nihil ipsa. Nisi.",
		"qs": queryset,
		# "specs" : special,
	}
	return render(request, "products/index.html", context)

def product_detail_view(request, pk=None, *args, **kwargs):
	# post = get_object_or_404(Product, pk=pk)
	# qs = Product.objects.filter(id=pk)
	# if qs.exists() and qs.count() == 1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404('Product Does not exist')
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist")

	context ={
		"prod" : instance
	}
	return render(request, "products/prod_details.html", context)

# class ProductDetailSlugView(DetailView):
# 	queryset = Product.objects.all()
# 	template_name = "products/prod_details.html"

# 	def get_object(self, *args, **kwargs):
# 		request = self.request
# 		slug = self.kwargs.get('slug')
# 		# instance = get_object_or_404(Product, slug=slug, active=True)
# 		# if instance is None:
# 		# 	raise Http404("Product don't exist")
# 		try:
# 			instance = Product.objects.get(slug=slug, active=True)
# 		except Product.DoesNotExist:
# 			raise Http404("Not FOund")
# 		except Product.MultipleObjectsReturned:
# 			qs = Product.objects.filter(slug=slug, active=True)
# 			instance = qs.first()
# 		except:
# 			raise Http404("Null")

# 		return instance

# def search(request):

#     product_list = Product.objects.all()[:10]
# 	rand_list = random.shuffle(product_list)
#     product_filter = ProductFilter(request.GET, queryset=product_list)
#     return render(request, 'products/product_list.html', {'filter': product_filter})

# def search(request):
# 	product_list = Product.objects.all()
# 	# rand_list = random.shuffle(product_list)
# 	product_filter = ProductFilter(request.GET, queryset=product_list)
# 	return render(request, "products/product_list.html", {"filter":product_filter})
