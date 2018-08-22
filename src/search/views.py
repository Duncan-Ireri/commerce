from django.db.models import Q 
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from products.models import Product

class SearchProductView(ListView):
    template_name='search/view.html'

    def get_context_data(self, *args, **kwargs):
    	context = super(SearchProductView, self).get_context_data(*args, **kwargs)
    	query = self.request.GET.get('q')
    	context['query'] = query
    	# SearchProductView.objects.create(query=query)
    	return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            lookups = Q(title__icontains = query) | Q(description__icontains=query)
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none()
