from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

app_name = "notes"


urlpatterns = [
    path(
        r"",
        NoteViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        r"<int:pk>/",
        NoteViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
