"""CoinApp Currency API Urls.

This file has the urls used
for currency api module.
"""
from django.conf.urls import url

from currency.api import views

# Currency views

currency_list = views.CurrencyViewSet.as_view({
    'get': 'list'
})

currency_create = views.CurrencyViewSet.as_view({
    'post': 'create'
})

currency_detail = views.CurrencyViewSet.as_view({
    'get': 'retrieve'
})

currency_update = views.CurrencyViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update'
})

currency_destroy = views.CurrencyViewSet.as_view({
    'delete': 'destroy'
})

urlpatterns = [
    url(
        r'^create-currency/$',
        currency_create,
        name='create-currency-api'
    ),
    url(
        r'^detail-currency/(?P<currency_id>[0-9]+)/$',
        currency_detail,
        name='detail-currency-api'
    ),
    url(
        r'^list-currencies/$',
        currency_list,
        name='list-currencies-api'
    ),
    url(
        r'^update-currency/(?P<currency_id>[0-9]+)/$',
        currency_update,
        name='update-currency-api'
    ),
    url(
        r'^deactivate-currency/(?P<currency_id>[0-9]+)/$',
        currency_destroy,
        name='deactivate-currency-api'
    )
]
