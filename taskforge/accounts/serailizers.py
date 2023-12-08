from rest_framework.serializers import ModelSerializer
from .models import User


class UserRegisterSeralizer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "profile_image"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
            "profile_image": {"read_only": True},
        }
