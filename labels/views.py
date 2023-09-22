from .serializers import LabelSerializer
from .models import Label
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter


class ReadOnlyLabelViewSet(ReadOnlyModelViewSet):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
