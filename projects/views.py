from django.db.models.query import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer
from rest_framework.filters import SearchFilter
from .models import Project
from .permissions import IsProductOwnerOrReadOnly


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    permission_classes = (IsAuthenticated, IsProductOwnerOrReadOnly)

    def get_queryset(self):
        current_user = self.request.user
        return Project.objects.filter(Q(owner=current_user) | Q(members=current_user))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
