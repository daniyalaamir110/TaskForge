from django.urls import path
from .views import UserViewSet

app_name = "accounts"

urlpatterns = [
    path(r"", UserViewSet.as_view({"get": "list", "post": "create"}), name="create")
]
