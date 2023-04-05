from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
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


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=256, verbose_name='Название категории', unique=True
    )


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category'
    )

    name = models.CharField(
        max_length=256, verbose_name='Название товара', unique=True
    )

    image = models.ImageField(
        upload_to='products/', verbose_name='Изображение'
    )

    price = models.IntegerField(
        default=1, verbose_name='Цена'
    )

    remain = models.IntegerField(
        default=1, verbose_name='Остаток'
    )

    short_description = models.CharField(
        max_length=256, verbose_name='Краткое описание'
    )

    description = models.TextField(
        max_length=512, verbose_name='Описание'
    )
