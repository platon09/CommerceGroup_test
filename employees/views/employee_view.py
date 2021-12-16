from rest_framework import viewsets
from employees.models import Employee
from employees.serializers import employee_serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.root_nodes()
    serializer_class = employee_serializer
    permission_classes = [IsAuthenticatedOrReadOnly]