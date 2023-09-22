from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, UpdateUserView, ReadOnlyUserViewSet

app_name = "accounts"

read_only_user_router = DefaultRouter()
read_only_user_router.register("", ReadOnlyUserViewSet)

urlpatterns = [
    path("", include(read_only_user_router.urls), name="user"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("update/", UpdateUserView.as_view(), name="update"),
]
