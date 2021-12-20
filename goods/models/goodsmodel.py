from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Category(models.Model):
    title = models.CharField(verbose_name='Название Категории', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Картегории'


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price='10000')


class GoodItem(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата добавления', auto_created=True, auto_now_add=True)
    title = models.CharField(verbose_name='Название', max_length=255)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    vendor = models.CharField(verbose_name='Поставщик', max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    new_category = models.ManyToManyField(Category, related_name='new_category')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = CustomManager()
    # on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'
