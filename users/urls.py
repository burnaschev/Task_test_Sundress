from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('users/api/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
