from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Order
from config.settings import TELEGRAM_BOT_TOKEN  # Подставьте вашу логику для получения токена
import requests


@receiver(post_save, sender=Order)
def send_telegram_notification(sender, instance, **kwargs):
    # Проверяем, был ли создан новый заказ
    if kwargs.get('created', False):
        # Формируем текст сообщения
        message_text = f"Получен новый заказ:\n"
        message_text += f"Номер заказа: {instance.id}\n"
        message_text += f"Тел: {instance.phone}\n"
        message_text += f"Имя: {instance.name}\n"
        message_text += f"Email: {instance.email}\n"
        # Добавьте другие необходимые поля

        # Отправляем сообщение в Telegram
        chat_id = "-4084669223"  # Замените на ваш реальный chat_id
        bot_token = TELEGRAM_BOT_TOKEN  # Замените на ваш реальный токен
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message_text}

        try:
            requests.post(url, json=payload)
        except Exception as e:
            # Обработка ошибки отправки в Telegram
            print(f"Ошибка отправки сообщения в Telegram: {e}")