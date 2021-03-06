from django.conf import settings

from django.contrib.auth.models import AbstractUser

from django.contrib.gis.db import models
from djmoney.models.fields import CurrencyField, MoneyField

from .currencies import CURRENCIES

class User(AbstractUser):
    phone = models.CharField(
                max_length=30,
                )
    language = models.CharField(
                    max_length=7,
                    choices=settings.LANGUAGES)
    currency = CurrencyField(
                    default='USD',
                    choices=CURRENCIES)

    class Meta:
        ordering = ('date_joined',)

class Area(models.Model):
    created = models.DateTimeField(
                auto_now_add=True,
                )
    name = models.CharField(
                max_length=100,
                )
    price = MoneyField(
                max_digits=100,
                decimal_places=2,
                default=0,
                default_currency='USD'
                )
    owner = models.ForeignKey(
                User,
                related_name='areas',
                on_delete=models.CASCADE,
                )
    area = models.MultiPolygonField()

    class Meta:
        ordering = ('created','name')

    def __str__(self):
        return self.name
