from django.urls import path
from .views import UserViewSet, ProfileImageViewset

app_name = "accounts"

urlpatterns = [
    path(
        r"",
        UserViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        r"<str:username>/",
        UserViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        r"<str:username>/profile_image/",
        ProfileImageViewset.as_view(
            {
                "put": "update_profile_image",
                "delete": "remove_profile_image",
            }
        ),
    ),
]
