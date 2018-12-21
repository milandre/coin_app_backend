"""CoinApp Currency models.

This file has the database models used
for currency module.
"""

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

from users.models import Client

# Create your models here.

class Currency(models.Model):
    """Currency model

    Fields:
      currency_id (char): Primary key. Code of the
                          Currency object
      name (char): Name of the currency
      closed (bool): True if the currency is a 
                     cryptocurrency, otherwise false.
                     Default: False
      created_at (date): Date of object creation
      last_update (date): Last updated date
    """

    currency_id = models.CharField(max_length=3, 
                                   unique=True, 
                                   primary_key=True)
    name = models.CharField(max_length=50)
    is_crypto = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + ' (' + self.currency_id + ')' 


class ExchangeRate(models.Model):
    """ExchangeRate model

    Fields:
      source_currency (obj): Related source currency.
                             ForeignKey to Currency
      target_currency (obj): Related target currency.
                             ForeignKey to Currency
      rate (float): Rate number for exchange
      from_date (date): Rate valid start date
      to_date (date): Rate valid end date
      created_at (date): Date of object creation
      last_update (date): Last updated date
    """

    source_currency = models.ForeignKey(Currency, 
                                        related_name='source_currency', 
                                        on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, 
                                        related_name='target_currency',
                                        on_delete=models.CASCADE)   
    rate = models.FloatField(validators=[MinValueValidator(0.0)])
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()

    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.source_currency + ' to ' + self.target_currency       