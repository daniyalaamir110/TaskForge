from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.contrib.auth.models import User


class ReadOnlyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
        )


class RegisterUserSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=8, max_length=20, required=True)
    confirm_password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "confirm_password",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
            "username": {"required": True},
        }

    def validate(self, attrs):
        password = attrs.get("password", None)
        confirm_password = attrs.get("confirm_password", None)

        if password != confirm_password:
            raise ValidationError({"password": "Passwords didn't match"})

        return attrs

    def create(self, validated_data):
        data = {
            "first_name": validated_data.get("first_name", None),
            "last_name": validated_data.get("last_name", None),
            "email": validated_data.get("email", None),
            "username": validated_data.get("username", None),
        }

        user = User.objects.create(**data)

        user.set_password(validated_data.get("password", None))

        user.save()

        return user


class UpdateUserSerializer(ModelSerializer):
    current_password = CharField(write_only=True)
    new_password = CharField(
        write_only=True, min_length=8, max_length=20, required=False
    )
    confirm_password = CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "current_password",
            "new_password",
            "confirm_password",
        )
        extra_kwargs = {"id": {"read_only": True}, "username": {"read_only": True}}

    def validate(self, attrs):
        user = attrs.get("user")
        data = {"user": user}

        first_name = attrs.get("first_name", None)
        last_name = attrs.get("last_name", None)
        email = attrs.get("email", None)
        current_password = attrs.get("current_password", None)
        new_password = attrs.get("new_password", None)
        confirm_password = attrs.get("confirm_password", None)

        if not user.check_password(current_password):
            raise AuthenticationFailed(
                {
                    "current_password": "Incorrect current password",
                }
            )

        if first_name:
            data["first_name"] = first_name

        if last_name:
            data["last_name"] = last_name

        if email:
            data["email"] = email

        if new_password:
            if new_password != confirm_password:
                raise ValidationError(
                    {
                        "password": "Passwords didn't match",
                    }
                )
            data["password"] = new_password

        return data

    def create(self, validated_data):
        user = validated_data.get("user", None)
        password = validated_data.get("password", None)

        if password:
            user.set_password(password)

        user.first_name = validated_data.get("first_name", user.first_name)
        user.last_name = validated_data.get("last_name", user.last_name)
        user.email = validated_data.get("email", user.email)

        user.save()

        return user
