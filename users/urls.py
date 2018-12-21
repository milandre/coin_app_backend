"""User urls.

This file has the urls used
for user module.
"""
from django.conf.urls import include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms

from .views import SignUpView

urlpatterns = [    
    re_path(
        r'^login/$', 
        auth_views.LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='login.html'),
        name='login'
    ),
    re_path(
        r'^logout/$', 
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    re_path(
        r'^signup/', 
        SignUpView.as_view(), 
        name='signup'
    )
]