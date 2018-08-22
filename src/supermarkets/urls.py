from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_stores, name='get_stores'),
    # path('ss/', views.get_stores_json, name='get_stores_json'),
]