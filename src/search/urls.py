from django.urls import path
# from products.views import product_list
from .views import SearchProductView

urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]