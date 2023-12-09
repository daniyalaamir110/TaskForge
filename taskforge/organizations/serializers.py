from rest_framework.serializers import ModelSerializer
from .models import Organization, Designation, Member


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
            "organization",
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


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = [
            "id",
            "organization",
            "member",
            "designation",
            "is_admin",
            "added_by",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "organization": {"read_only": True},
            "member": {"required": True},
            "designation": {"required": True},
            "is_admin": {"read_only": True},
            "added_by": {"read_only": True},
            "active": {"read_only": True},
        }
