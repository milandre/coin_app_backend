"""Client API urls.

Urls for Client API.
"""

from rest_framework.authtoken import views
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]