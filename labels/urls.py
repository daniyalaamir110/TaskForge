from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReadOnlyLabelViewSet

app_name = "labels"

read_only_label_router = DefaultRouter()
read_only_label_router.register("", ReadOnlyLabelViewSet)

urlpatterns = [path("", include(read_only_label_router.urls), name="label")]
