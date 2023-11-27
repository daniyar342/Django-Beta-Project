from django.contrib import admin
from .models import Product,SubCategory,Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "name",
        "compound",
        'description',
        'applying',
        'waiting_time',
        'release',
        'storage_date',
        'storage_conditions',
        'sub_category',
    ]
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'category'
    ]
    prepopulated_fields = {'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
    ]
    prepopulated_fields = {'slug':('name',)}