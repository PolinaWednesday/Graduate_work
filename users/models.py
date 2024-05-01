from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='отчество', **NULLABLE)
    phone = models.CharField(max_length=12, verbose_name='телефон', **NULLABLE)
    birth_date = models.DateField(verbose_name='дата рождения', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    verify_code = models.CharField(max_length=12, verbose_name='код верификации', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email_confirmation_token = models.CharField(max_length=64, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.email_confirmation_token:
            self.email_confirmation_token = default_token_generator.make_token(self)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
