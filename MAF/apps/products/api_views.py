from .models import Product, Order
from rest_framework import viewsets
from .serializer import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CanPostProductPermission
from .token import TOKEN


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CanPostProductPermission]


class ApiApplicationView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    context_object_name = 'orders'

    def create(self, request, requests=None, *args, **kwargs):
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



# For example (code):
#
# from telegram import Bot
# from telegram.ext import Updater
#
# API_TOKEN = "your_bot_token"
# API_ID = "your_api_id"
# API_HASH = "your_api_hash"
#
# bot = Bot(token=API_TOKEN)
# updater = Updater(token=API_TOKEN, use_context=True)
#
# # Now you can start adding functionality to your bot using the 'bot' and 'updater' objects.

# Обязательно замените «your_bot_token», «your_api_id» и «your_api_hash» фактическими
# значениями, которые вы получили. Запустите своего бота: запустите свой код, и теперь
# ваш бот должен быть подключен к API Telegram, используя предоставленный идентификатор API,
# хэш API и токен бота. Не забывайте сохранять конфиденциальность своего API-идентификатора,
# хеша API и токена бота и не разглашать их публично. Если вы работаете над общедоступным
# проектом, рассмотрите возможность использования переменных среды или файла конфигурации
# для безопасного хранения этих конфиденциальных значений.