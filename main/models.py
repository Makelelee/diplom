from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def str(self):
        return f'{self.full_name} ({self.username})'

    @property
    def full_name(self):
        return self.get_full_name()

    phone = models.CharField(
        max_length=64, verbose_name='Номер телефона', null=True, blank=True, unique=True
    )

    nickname = models.CharField(
        max_length=64, verbose_name='Ник', null=True, blank=True, unique=True
    )
