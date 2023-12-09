from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from common.utils import get_queryset_with_deleted
from common.paginations import StandardResultsSetPagination
from .serializers import NoteSerailizer
from .models import Note


class NoteViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerailizer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title"]

    def get_queryset(self):
        queryset = Note.objects.filter(author=self.request.user.id)
        queryset = get_queryset_with_deleted(self, queryset)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
