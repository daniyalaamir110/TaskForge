from django.urls import path
from .views import ProjectViewset

app_name = "projects"


urlpatterns = [
    path(
        "",
        ProjectViewset.as_view({"get": "list", "post": "create"}),
        name="project",
    ),
    path(
        "<int:pk>/",
        ProjectViewset.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project",
    ),
]
