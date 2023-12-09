from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from common.paginations import StandardResultsSetPagination
from common.utils import get_queryset_with_deleted
from .models import Organization, Designation
from .serializers import OrganizationSerializer, DesignationSerializer


class OrganizationViewset(ModelViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]

    def get_queryset(self):
        queryset = Organization.objects.filter(founder=self.request.user.id)
        queryset = get_queryset_with_deleted(self, queryset)
        return queryset

    def perform_create(self, serializer):
        return serializer.save(founder=self.request.user)


class DesignationViewset(ModelViewSet):
    serializer_class = DesignationSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title"]

    def get_organization_id(self):
        return self.kwargs["organization_id"]

    def get_queryset(self):
        queryset = Designation.objects.filter(organization=self.get_organization_id())
        queryset = get_queryset_with_deleted(self, queryset)
        return queryset

    def perform_create(self, serializer):
        organization = Organization.objects.get(id=self.get_organization_id())
        return serializer.save(organization=organization)
