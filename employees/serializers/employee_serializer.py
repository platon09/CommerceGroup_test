from rest_framework import serializers
from employees.models import Employee
from rest_framework_recursive.fields import RecursiveField

class EmployeeSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position', 'employment_date', 'salary', 'children')