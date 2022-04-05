from django.shortcuts import render
from html5lib import serialize

from rest_framework import viewsets, mixins

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,        
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    """
    Employees Json List |
    Lista de Empregados em Json
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer