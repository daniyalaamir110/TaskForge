from rest_framework.serializers import ModelSerializer
from .models import Task
from labels.serializers import LabelSerializer
from accounts.serializers import ReadOnlyUserSerializer
from projects.serializers import ProjectSerializer


class TaskSerializer(ModelSerializer):
    label_details = LabelSerializer(many=True, read_only=True)
    assignee = ReadOnlyUserSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["status", "label_details"]
        extra_kwargs = {"labels": {"write_only": True}}


class UpdateTaskStatusSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = (
            "id",
            "title",
            "description",
            "due_date",
            "priority",
            "labels",
            "project",
            "assigned_to",
            "created_at",
            "updated_at",
        )
