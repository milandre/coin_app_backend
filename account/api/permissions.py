"""Account API permissions

This file has custom permissions.
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow
    owners of an object to edit it.

    Assumes the model instance has an `client`
    attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `client`.
        return obj.client == request.user


class IsOwnerTransaction(permissions.BasePermission):
    """
    Object-level permission to only allow
    owners of an object to see it.

    Assumes the model instance has an `account_from`
    attribute.
    """

    def has_object_permission(self, request, view, obj):
        
        # Instance must have an attribute named `account_from`.
        return obj.account_from.client == request.user