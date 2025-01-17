from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None  # поле удалится
    # заменим его на email, который нужно переопределить:
    email = models.EmailField(unique=True, verbose_name='почта')  # поле уникальное

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=200, verbose_name='страна', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='статус активности')

    email_verify_token = models.CharField(max_length=50, **NULLABLE,
                                          verbose_name='код верификации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('is_active',)
        permissions = [
            ('can_block_user', 'Может блокировать пользователя'),
        ]
