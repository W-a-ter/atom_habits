from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True, verbose_name='Имя пользователя', default=0)
    tg_chat_id = models.CharField(max_length=50, unique=True, verbose_name='Телеграм чат-id', default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
