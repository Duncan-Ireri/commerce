from django.shortcuts import render
from django.views.generic import DetailView, ListView
from products.models import Product

class SearchProductView(ListView):
    template_name='search/view.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none()
