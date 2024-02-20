from django.contrib import admin
from cotalog.models import Category, Plant, Image, Variety


class ImageInline(admin.StackedInline):
    extra = 1
    model = Image


class VarietyInline(admin.StackedInline):
    extra = 1
    model = Variety


class PlantInline(admin.StackedInline):
    extra = 1
    model = Plant


class CategoryAdmin(admin.ModelAdmin):
    inlines = [VarietyInline]
    list_filter = [
        'id',
        'title',
        'created_at',
        'updated_at'
    ]
    list_display = [
        'id',
        'title',
        'image',
        'created_at',
        'updated_at'
    ]


class VarietyAdmin(admin.ModelAdmin):
    inlines = [PlantInline]
    list_filter = [
        'id',
        'title',
        'created_at',
        'updated_at'
    ]
    list_display = [
        'id',
        'title',
        'category',
        'created_at',
        'updated_at'
    ]


class PlantAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ['title']
    readonly_fields = ['slug']
    list_filter = [
        'id',
        'title',
        'price',
        'created_at',
        'updated_at'
    ]
    list_display = [
        'id',
        'title',
        'description',
        'price',
        'variety',
        'mesurement_unit',
        'created_at',
        'updated_at'
    ]


class ImageAdmin(admin.ModelAdmin):
    list_filter = [
        'id',
        'created_at',
        'updated_at'
    ]
    list_display = [
        'id',
        'image',
        'undertitle',
        'plant',
        'created_at',
        'updated_at'
    ]


admin.site.register(Variety, VarietyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(Image, ImageAdmin)
