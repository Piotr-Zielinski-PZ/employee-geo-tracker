from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from group_service.viewsets import GroupViewSet
from location_service.viewsets import LocationViewSet
from task_service.viewsets import TaskViewSet
from user_service.viewsets import UserViewSet


router = SimpleRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"groups", GroupViewSet, basename="group")
router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"locations", LocationViewSet, basename="location")

urlpatterns = [
    path("admin/", admin.site.urls),
] + router.urls
