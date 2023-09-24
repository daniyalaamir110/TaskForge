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
