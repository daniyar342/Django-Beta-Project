# from django.contrib import admin
# from django.urls import path, include
# from .views import *
#
# urlpatterns = [
#     path("list_products/", Index.as_view(), name="list"),
#     path("api/v1/productlist/", Index.as_view()),
# ]

def l9l9n_message():
    """
        Короче здесь products.urls.py нам нахуй не нужна!!!
        Вся хуйня находится в главном config.urls.py
        Весь маршрут проходит там и через include подключает router который всех посылает нах! :) шучу!
        Там всё будет так:  api/v1/product
                            api/v1/blog
    """
    pass