from django.db import models


class ExchangeRate(models.Model):
    date = models.DateField()
    currency = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
