from django.urls import path
from .views import ProjectViewSet, ProjectMemberViewSet

app_name = "projects"


urlpatterns = [
    path(
        "",
        ProjectViewSet.as_view({"get": "list", "post": "create"}),
        name="project",
    ),
    path(
        "<int:pk>/",
        ProjectViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project",
    ),
    path(
        "<int:pk>/members/",
        ProjectMemberViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project",
    ),
]
