from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerailizer(ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "body", "created_at", "updated_at"]
