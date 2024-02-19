from django.contrib import admin
from cotalog.models import Category, Plant


# class PlantAdmin(admin.ModelAdmin):
#     filter_horizontal = ['category']


admin.site.register(Category)
admin.site.register(Plant)
