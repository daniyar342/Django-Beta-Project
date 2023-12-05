import requests
from rest_framework import generics, viewsets
from rest_framework.generics import mixins
from .models import Product, Order
from .serializer import ProductSeializer, OrderSerializer

from .token import TOKEN


class Index(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeializer
    context_object_name = 'products'


class ApiApplicationView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    context_object_name = 'orders'

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Получение данных из запроса
        data = request.data

        # Формирование текста сообщения для отправки
        message_text = "Получена новая заявка:\n"
        for key, value in data.items():
            if key in ["name", "email", "number"]:
                message_text += f"{key}: {value}\n"

        # Отправка сообщения в Telegram
        chat_id = "-1001740033990"
        bot_token = TOKEN
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message_text}
        requests.post(url, json=payload)

        return response
