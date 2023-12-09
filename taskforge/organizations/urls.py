from django.urls import path
from .views import OrganizationViewset, DesignationViewset, MemberViewset

app_name = "organizations"

urlpatterns = [
    path(
        r"",
        OrganizationViewset.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        r"<int:pk>/",
        OrganizationViewset.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        r"<int:organization_id>/designations/",
        DesignationViewset.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        r"<int:organization_id>/designations/<int:pk>/",
        DesignationViewset.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        r"<int:organization_id>/members/",
        MemberViewset.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        r"<int:organization_id>/members/<int:pk>/",
        MemberViewset.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
