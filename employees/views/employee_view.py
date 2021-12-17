from rest_framework import viewsets
from employees.models import Employee
from employees.serializers.employee_serializer import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.get_tree()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'first_name', 'last_name', 'position', 'employment_date', 'salary']
    ordering_fields = ['id', 'first_name', 'last_name', 'position', 'employment_date', 'salary']



