from rest_framework.serializers import ModelSerializer
from .models import Label


class LabelSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Label
