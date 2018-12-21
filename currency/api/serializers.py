"""Currency serializer.

This file has the Currency module
serializers.
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from currency.models import Currency, ExchangeRate


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'
        

class ExchangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = '__all__'