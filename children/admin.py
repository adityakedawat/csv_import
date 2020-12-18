from django.contrib import admin
from .models import children

@admin.register(children)
class childrenAdmin(admin.ModelAdmin):
	list_display=['name','sex','age']