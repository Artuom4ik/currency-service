from django.db import models


class ExchangeRate(models.Model):
    date = models.DateField(verbose_name="Дата курса")
    currency_id = models.IntegerField(max_length=10, verbose_name="ID валюты")
    currency_name = models.CharField(max_length=10, verbose_name="Валюта")
    scale = models.IntegerField(verbose_name="Количество")
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name="Курс"
    )
