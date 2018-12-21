"""Account serializer.

This file has the Account module
serializers.
"""

from rest_framework import serializers

from account.models import Account, Transaction
from currency.models import Currency
from users.models import Client

from currency.api.serializers import CurrencySerializer
from users.api.serializers import ClientSerializer


class AccountSerializer(serializers.ModelSerializer):

    client = ClientSerializer(read_only=True)
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    account_from = AccountSerializer(read_only=True)
    account_to = AccountSerializer(read_only=True)
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'