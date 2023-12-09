from rest_framework.serializers import ModelSerializer
from .models import Organization, Designation, MemberOrganization


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "id",
            "name",
            "description",
            "founder",
            "active",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "name": {"required": True},
            "description": {"required": True},
            "founder": {"read_only": True},
            "active": {"read_only": True},
        }


class DesignationSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = [
            "id",
            "title",
            "description",
            "active",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "title": {"required": True},
            "description": {"required": True},
            "organization": {"read_only": True},
            "active": {"read_only": True},
        }
