"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from rest_framework.routers import SimpleRouter

from group_service.viewsets import GroupViewSet
from location_service.viewsets import LocationViewSet
from task_service.viewsets import TaskViewSet
from user_service.viewsets import UserViewSet

router = SimpleRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"locations", LocationViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
] + router.urls
