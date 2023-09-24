from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from rest_framework.filters import SearchFilter
from .models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from projects.models import Project
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("title",)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user).order_by("-updated_at")

    @action(detail=False, methods=["post"])
    def create(self, request, pk=None):
        project_id = request.data.get("project")
        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response(
                {"detail": "Project not found"},
                status=HTTP_404_NOT_FOUND,
            )

        if project.owner != request.user:
            return Response(
                {"detail": "You don't own this project"},
                status=HTTP_403_FORBIDDEN,
            )

        return super().create(request=request, pk=pk)

    @action(detail=True, methods=["patch"])
    def update(self, request, pk):
        task = self.get_object()
        project = task.project

        if project.owner != request.user:
            return Response(
                {"detail": "You don't own this project"},
                status=HTTP_403_FORBIDDEN,
            )

        return super().update(request=request, pk=pk)

    @action(detail=True, methods=["delete"])
    def destroy(self, request, pk):
        task = self.get_object()
        project = task.project

        if project.owner != request.user:
            return Response(
                {"detail": "You don't own this project"},
                status=HTTP_403_FORBIDDEN,
            )

        if task.status == "completed":
            return Response(
                {"detail": "The task has completed"},
                status=HTTP_403_FORBIDDEN,
            )

        return super().destroy(request=request, pk=pk)

    @action(detail=True, methods=["patch"])
    def partial_update(self, request, pk=None):
        project_id = request.data.get("project")
        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response(
                {"detail": "Project not found"},
                status=HTTP_404_NOT_FOUND,
            )

        if project.owner != request.user:
            return Response(
                {"detail": "You don't own this project"},
                status=HTTP_403_FORBIDDEN,
            )

        return super().create(request=request, pk=pk)
