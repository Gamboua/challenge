from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        """
        Removi o campo 'id' para ficar compativel com o json modelo que me encaminharam
        """
        fields = ('name', 'email', 'department')
