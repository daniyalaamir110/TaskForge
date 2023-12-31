"""
URL configuration for taskforge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Taskforge API",
        default_version="v1",
        contact=openapi.Contact(email="daniyal.amir110@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
).with_ui("swagger", cache_timeout=0)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("auth/", include("authn.urls"), name="auth"),
    path("notes/", include("notes.urls"), name="notes"),
    path("organizations/", include("organizations.urls"), name="organizations"),
    path("api-docs/", schema_view, name="swagger"),
]
