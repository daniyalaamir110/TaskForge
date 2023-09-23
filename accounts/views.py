from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter
from .serializers import (
    RegisterUserSerializer,
    UpdateUserSerializer,
    ReadOnlyUserSerializer,
)
from django.contrib.auth.models import User


class ReadOnlyUserViewSet(ReadOnlyModelViewSet):
    serializer_class = ReadOnlyUserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    search_fields = ("first_name", "last_name", "username", "email")


class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)


class UpdateUserView(CreateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
