"""CoinApp Currency API views

This file has the all api
currency operations.
"""

from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from currency.models import Currency
#from permissions import IsOwnerOrReadOnly
from .serializers import CurrencySerializer

# Currency Viewset


class CurrencyViewSet(viewsets.ModelViewSet):
    """CurrencyViewSet

    ModelViewSet for Currency objects. Include
    create(), retrieve(), update(), list(), 
    destroy() operations
    """

    queryset = Currency.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_url_kwarg = 'currency_id'
    serializer_class = CurrencySerializer

    def create(self, request, *args, **kwargs):
        """Create a Currency object.

        Returns:
            A 201 HTTP Response indicating
            the Currency creation, otherwise
            an exception raise
        """
        # Serialize the information in request.data
        serializer = self.get_serializer(data=request.data)
        # Check if is valid
        serializer.is_valid(raise_exception=True)

        # If serializer is valid, then save the object
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)