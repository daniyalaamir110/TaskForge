from django.urls import path
from .views import TaskViewSet, UpdateTaskStatusView

app_name = "tasks"

urlpatterns = [
    path(
        "",
        TaskViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="task",
    ),
    path(
        "<int:pk>/",
        TaskViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="task",
    ),
    path(
        "<int:pk>/status",
        UpdateTaskStatusView.as_view(),
        name="task_status",
    ),
]
