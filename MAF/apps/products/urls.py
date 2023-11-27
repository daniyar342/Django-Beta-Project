from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("list_products/", Index.as_view(), name="list"),
    ]