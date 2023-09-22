from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import (
    RegisterUserSerializer,
    UpdateUserSerializer,
    ReadOnlyUserSerializer,
)
from django.contrib.auth.models import User


class ReadOnlyUserViewSet(ReadOnlyModelViewSet):
    serializer_class = ReadOnlyUserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UpdateUserView(CreateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
