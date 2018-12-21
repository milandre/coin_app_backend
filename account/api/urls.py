"""CoinApp Account API Urls.

This file has the urls used
for account api module.
"""
from django.conf.urls import url

from account.api import views

# Account views

account_list = views.AccountViewSet.as_view({
    'get': 'list'
})

account_create = views.AccountViewSet.as_view({
    'post': 'create'
})

account_detail = views.AccountViewSet.as_view({
    'get': 'retrieve'
})

account_update = views.AccountViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update'
})

account_destroy = views.AccountViewSet.as_view({
    'delete': 'destroy'
})

# Transaction views

transaction_list = views.TransactionViewSet.as_view({
    'get': 'list'
})

transaction_create = views.TransactionViewSet.as_view({
    'post': 'create'
})

transaction_detail = views.TransactionViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(
        r'^create-account/$',
        account_create,
        name='create-account-api'
    ),
    url(
        r'^detail-account/(?P<account_id>[0-9]+)/$',
        account_detail,
        name='detail-account-api'
    ),
    url(
        r'^list-accounts/$',
        account_list,
        name='list-accounts-api'
    ),
    url(
        r'^list-accounts-by-user/(?P<email>.+)/$',
        views.ListAccountsByUser.as_view(),
        name='list-accounts-by-user-api'
    ),
    url(
        r'^update-account/(?P<account_id>[0-9]+)/$',
        account_update,
        name='update-account-api'
    ),
    url(
        r'^deactivate-account/(?P<account_id>[0-9]+)/$',
        account_destroy,
        name='close-account-api'
    ),
    url(
        r'^create-transaction/$',
        transaction_create,
        name='create-transaction-api'
    ),
    url(
        r'^detail-transaction/(?P<transaction_id>[0-9]+)/$',
        transaction_detail,
        name='detail-transaction-api'
    ),
    url(
        r'^list-transactions/$',
        transaction_list,
        name='list-transactions-api'
    ),
    url(
        r'^list-transactions-by-user/(?P<email>.+)/$',
        views.ListTransactionsByUser.as_view(),
        name='list-transactions-by-user-api'
    ),
]
