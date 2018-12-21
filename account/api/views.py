"""CoinApp Account API views

This file has the all api account
operations.
"""
from django.db.models import Q

from rest_framework import generics, status
from rest_framework import viewsets, mixins
from rest_framework.authentication import (
    BasicAuthentication
)

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from account.models import Account, Transaction
from currency.models import Currency
from .permissions import IsOwnerOrReadOnly, IsOwnerTransaction
from .serializers import AccountSerializer, TransactionSerializer

# Account Viewset


class AccountViewSet(viewsets.ModelViewSet):
    """AccountViewSet

    ModelViewSet for Account objects. Include
    create(), retrieve(), update(), list(), 
    destroy() operations
    """

    queryset = Account.objects.all()
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    lookup_url_kwarg = 'account_id'
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):
        """Create a Account object.

        Returns:
            A 201 HTTP Response indicating
            the Account creation, otherwise
            an exception raise
        """
        # Getting currency id for later asociation with
        # Transaction object created
        currency_id = request.data['currency']
        # Serialize the information in request.data
        serializer = self.get_serializer(data=request.data)
        # Check if is valid
        serializer.is_valid(raise_exception=True)

        # If serializer is valid, then save the object
        self.custom_perform_create(serializer, currency_id)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def custom_perform_create(self, serializer, currency_id):
        """Perform the save operations.

        Returns:
            An Account creation in database
        """
        # Creates the account
        currency = Currency.objects.get(currency_id=currency_id)
        serializer.save(client=self.request.user, currency=currency)


class ListAccountsByUser(generics.ListAPIView):
    """ListAccountsByUser

    List accounts by user
    """
    queryset = Account.objects.all()    
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    http_method_names = [u'get']
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(client__email=self.kwargs['email'])
        return queryset



# Transaction Viewset

class TransactionViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """TransactionViewSet

    GenericViewSet for Transaction objects. Include
    create(), list() and retrieve() operations
    """

    queryset = Transaction.objects.all()
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerTransaction)
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        """Create a Transaction object.

        Returns:
            A 201 HTTP Response indicating
            the Transaction creation, otherwise
            an exception raise
        """
        # Getting account_from id, account_to id and 
        # currency id for later asociation with
        # object Transaction created
        account_from_id = request.data['account_from']
        account_to_id = request.data['account_to']
        currency_id = request.data['currency']

        # Serialize the information in request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.custom_perform_create(serializer, 
                                   account_from_id, 
                                   account_to_id,
                                   currency_id)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def custom_perform_create(self, serializer, account_from_id,
                              account_to_id, currency_id):
        """Perform the save operations.

        Returns:
            A Transaction creation in database with the asociated
            Accounts and Currency object
        """
        # Creates the answer
        account_from = Account.objects.get(id=account_from_id)
        account_to = Account.objects.get(id=account_to_id)
        currency = Currency.objects.get(currency_id=currency_id)
        serializer.save(account_from=account_from, 
                        account_to=account_to,
                        currency=currency)


class ListTransactionsByUser(generics.ListAPIView):
    """ListTransactionsByUser

    List transactions by user
    """
    queryset = Transaction.objects.all()    
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    http_method_names = [u'get']
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(Q(account_from__client__email=self.kwargs['email'])|
                                        Q(account_to__client__email=self.kwargs['email']))
        return queryset