from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    SerializerMethodField,
)
from .models import Project
from accounts.serializers import ReadOnlyUserSerializer
from labels.serializers import LabelSerializer
from tasks.models import Task


class ProjectSerializer(ModelSerializer):
    member_count = IntegerField(read_only=True)
    top_members = ReadOnlyUserSerializer(many=True)
    is_owner = SerializerMethodField(method_name="get_is_owner", read_only=True)
    owner_details = SerializerMethodField(method_name="get_owner_details")

    class Meta:
        model = Project
        exclude = ["members", "owner"]
        extra_kwargs = {
            "owner": {"read_only": True},
        }

    def add_member(self, project, user):
        project.members.add(user)

    def remove_member(self, project, user):
        project.members.remove(user)

    def get_is_owner(self, project):
        return project.owner == self.context["request"].user

    def get_owner_details(self, project):
        owner_serializer = ReadOnlyUserSerializer(project.owner)
        return owner_serializer.data


class ProjectMemberSerializer(ModelSerializer):
    members = ReadOnlyUserSerializer(read_only=True, many=True)
    user_id = IntegerField(write_only=True, required=True)

    class Meta:
        model = Project
        fields = ["members", "user_id"]


class ProjectTaskSerializer(ModelSerializer):
    assignee = ReadOnlyUserSerializer()
    label_details = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ["status"]
