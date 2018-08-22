import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from .models import SuperSub

# Create your views here.
def get_stores(request):
    stores = SuperSub.objects.all()  #.values('lon', 'lat', 'substore')
    jsondata = serializers.serialize('json', stores)
    # return HttpResponse(jsondata, content_type='application/json')
    return render(request, "store/location.html", {"stores" : jsondata})


# def get_stores_json(request):
# 	stores = SuperSub.objects.all()
# 	stores_json = json.dumps(stores)
# 	return render(request, "store/location.html", {"stores" : stores_json})