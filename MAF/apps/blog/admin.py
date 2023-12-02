from django.contrib import admin
from .models import *


@admin.register(Events)
class BlogEventsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'created_at',
        'image'
    ]


@admin.register(Public)
class BlogPublicAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'created_at',
        'image'
    ]


@admin.register(New_Products)
class BlogNewProductsAdmin(admin.ModelAdmin):
    list_display = [
        'product_name'
    ]


@admin.register(Enxibitation_Calendar)
class BlogCalendarAdmin(admin.ModelAdmin):
    list_display = [
        'period',
        'data_of_participation',
        'location',
        'name_exhibition'
    ]
