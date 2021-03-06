from rest_framework import serializers
from django.db.models import Avg

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'name',
            'email',
            'department',
        )