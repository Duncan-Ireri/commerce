from django.contrib import admin

from .models import SuperName, SuperSize, SuperSub


admin.site.register(SuperName)
admin.site.register(SuperSize)
admin.site.register(SuperSub)