from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .serailizers import UserRegisterSeralizer
from .models import User
from common.paginations import StandardResultsSetPagination


class UserViewSet(ModelViewSet):
    serializer_class = UserRegisterSeralizer
    queryset = User.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["first_name", "last_name", "email", "username"]
    lookup_field = "username"
