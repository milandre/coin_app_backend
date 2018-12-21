# -*- coding: utf-8 -*-

"""User Admin

This file has the user database models register
for django admin module.
"""

from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .forms import SignUpAdminForm, ClientUpdateForm
from .models import Client

# Register your models here.

class ClientAdmin(AuthUserAdmin):
    # The forms to add and change user instances
    form = ClientUpdateForm
    add_form = SignUpAdminForm

    # The fields to be used in displaying the Client model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_active')
    list_filter = ('is_admin','is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
        ('Permissions', {'fields': ('is_admin','is_active',
                         'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','first_name','last_name')
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new ClientAdmin...
admin.site.register(Client, ClientAdmin)