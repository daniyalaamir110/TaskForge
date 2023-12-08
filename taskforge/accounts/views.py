from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from .serailizers import UserSeralizer, ProfileImageSerializer
from .models import User
from common.paginations import StandardResultsSetPagination
from common.utils import get_queryset_with_deleted
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class UserViewSet(ModelViewSet):
    serializer_class = UserSeralizer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name", "email", "username"]
    lookup_field = "username"

    def get_queryset(self):
        queryset = get_queryset_with_deleted(self, User.objects.all())
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "include_deleted", openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProfileImageViewset(ModelViewSet):
    serializer_class = ProfileImageSerializer
    parser_classes = [FormParser, MultiPartParser]
    lookup_field = "username"
    permission_classes = [IsAuthenticated]

    def update_profile_image(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            instance = serializer.save()
            profile_image_url = self.request.build_absolute_uri(
                instance.profile_image.url
            )
            return Response({"profile_image": profile_image_url}, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def remove_profile_image(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            request.user, data={"profile_image": None}, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(None, status=HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
