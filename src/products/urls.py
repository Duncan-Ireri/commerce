from django.urls import path
from . import views
# from .views import ProductDetailSlugView

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product-detail/<int:pk>/', views.product_detail_view, name='product_detail_view'),
    # path('product/<slug:slug>/', ProductDetailSlugView.as_view(), name="ProductDetailSlugView"),
    # path('search/', views.search, name='search'),
]