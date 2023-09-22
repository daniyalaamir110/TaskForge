from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, UpdateUserView, ReadOnlyUserViewSet

app_name = "accounts"

urlpatterns = [
    path("", ReadOnlyUserViewSet.as_view({"get": "list"}), name="list"),
    path("<int:pk>/", ReadOnlyUserViewSet.as_view({"get": "retrieve"}), name="detail"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("update/", UpdateUserView.as_view(), name="update"),
]
