from django.db.models.query import Q
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer, ProjectMemberSerializer
from rest_framework.filters import SearchFilter
from .models import Project
from .permissions import IsProductOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import SAFE_METHODS
from accounts.serializers import ReadOnlyUserSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    permission_classes = (IsAuthenticated, IsProductOwnerOrReadOnly)

    def get_queryset(self):
        current_user = self.request.user
        return Project.objects.filter(Q(owner=current_user) | Q(members=current_user))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectMemberViewSet(ModelViewSet):
    serializer_class = ProjectMemberSerializer
    permission_classes = (IsAuthenticated, IsProductOwnerOrReadOnly)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ReadOnlyUserSerializer
        else:
            return ProjectMemberSerializer

    def get_queryset(self):
        if self.request.method in SAFE_METHODS:
            project_id = self.kwargs.get("pk")
            try:
                project = Project.objects.get(pk=project_id)
            except Project.DoesNotExist:
                raise NotFound("Product not found")

            return project.members.all()
        else:
            return Project.objects.all()

    @action(detail=True, methods=["post"])
    def create(self, request, pk=None):
        product = self.get_object()
        user_id = request.data.get("user_id")

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"},
                status=HTTP_404_NOT_FOUND,
            )

        if user in product.members.all():
            return Response(
                {"detail": "User already a member"},
                status=HTTP_400_BAD_REQUEST,
            )

        if user == product.owner:
            return Response(
                {"detail": "Owner can't be explicitly set as member"},
                status=HTTP_400_BAD_REQUEST,
            )

        product.members.add(user)
        return Response(
            {"detail": "Member added successfully"},
            status=HTTP_200_OK,
        )
