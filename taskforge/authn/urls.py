from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "auth"

urlpatterns = [
    path(r"login/", TokenObtainPairView.as_view(), name="get_token"),
    path(r"verify/", TokenVerifyView.as_view(), name="verify_token"),
    path(r"refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
