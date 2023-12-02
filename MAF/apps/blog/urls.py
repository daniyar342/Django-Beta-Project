from django.contrib import admin
from django.urls import path, include
from .views import BlogEvents, PublicBlogView

urlpatterns = [
    path("api/v1/blog_list/", BlogEvents.as_view()),
    path("api/v1/blog_pub/", PublicBlogView.as_view()),
]
