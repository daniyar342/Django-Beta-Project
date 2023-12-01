from django.contrib import admin
from .models import *
@admin.register(Events)
class BlogEventsAdmin(admin.ModelAdmin):
    pass

@admin.register(Public)
class BlogPublicAdmin(admin.ModelAdmin):
    pass

@admin.register(New_Products)
class BlogNewProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(Enxibitation_Calendar)
class BlogCalendarAdmin(admin.ModelAdmin):
    pass