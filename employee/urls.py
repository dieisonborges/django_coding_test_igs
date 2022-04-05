from os import name
from django.db import router
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import EmployeeViewSet

router = SimpleRouter()
router.register('', EmployeeViewSet)

urlpatterns = []
