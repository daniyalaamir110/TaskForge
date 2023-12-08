from rest_framework.serializers import ModelSerializer
from .models import User


class UserSeralizer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "profile_image",
            "active",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
            "active": {"read_only": True},
            "password": {"write_only": True, "required": True},
            "profile_image": {"read_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class ProfileImageSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_image"]
        extra_kwargs = {"profile_image": {"required": True}}
