from rest_framework.serializers import ModelSerializer
from .models import Project
from accounts.serializers import ReadOnlyUserSerializer
from django.contrib.auth.models import User


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        extra_kwargs = {
            "owner": {"read_only": True},
            "members": {"read_only": True},
        }
