"""Currency Admin

This file has the currency database models register
for django admin module.
"""
from django.contrib import admin

from .models import Currency

# Register your models here.
admin.site.register(Currency)