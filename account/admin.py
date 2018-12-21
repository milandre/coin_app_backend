"""Account Admin

This file has the user database models register
for django admin module.
"""
from django.contrib import admin

from .models import Account, Transaction

# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)