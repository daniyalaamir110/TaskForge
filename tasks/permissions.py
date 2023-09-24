from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsTaskAssignee(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.assignee != request.user:
            raise PermissionDenied("This task is not assigned to you")

        return super().has_object_permission(request, view, obj)
