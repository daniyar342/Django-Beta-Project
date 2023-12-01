from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("api/v1/blog_list/",BlogEvents.as_view())
    ]