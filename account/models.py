"""CoinApp Account models.

This file has the database models used
for account module.
"""

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

from users.models import Client
from currency.models import Currency

# Create your models here.

# Status of the transaction

class Account(models.Model):
    """Account model

    Fields:
      client (obj): ForeignKey to Client
      currency (obj): ForeignKey to Currency
      balance (float): Available amount of money
      created_at (date): Date of object creation
      last_update (date): Last updated date
    """

    client = models.ForeignKey(Client, 
                             related_name='accounts',
                             on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, 
                               related_name='accounts',
                               on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0,
                              validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(default=timezone.now)
    last_updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        result = self.client.email + ' - ' + self.currency.currency_id
        result += ' - ' +  str(self.balance)
        return result              


class Transaction(models.Model):
    """Transaction model

    Fields:
      account_from (obj): Related source account.
                          ForeignKey to Account
      account_to (obj): Related target account.
                        ForeignKey to Account
      currency (obj): Currency of the transaction
      amount (float): Amount of money of the transaction
      created_at (date): Date of object creation
    """

    account_from = models.ForeignKey(Account, 
                                   related_name='account_from_transactions',
                                   on_delete=models.CASCADE
                                   )
    account_to = models.ForeignKey(Account, 
                                 related_name='account_to_transactions',
                                 on_delete=models.CASCADE
                                 )
    currency = models.ForeignKey(Currency, 
                               related_name='transactions',
                               on_delete=models.CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        result = self.account_from.client.email + ' to ' + self.account_to.client.email + ' - '
        result += self.currency.currency_id + ' - ' + str(self.amount)
        return result 
               
    
        