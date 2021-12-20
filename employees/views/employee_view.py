from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from employees.models import Employee
from employees.serializers.employee_serializer import EmployeeSerializer, CreateEmployeeSerializer
from rest_framework import filters

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.get_tree()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'first_name', 'last_name', 'position', 'employment_date', 'salary']
    ordering_fields = ['id', 'first_name', 'last_name', 'position', 'employment_date', 'salary']

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateEmployeeSerializer
        return EmployeeSerializer

    def create(self, request, *args, **kwargs):
        parent_id = request.data.pop('parent_id')
        try:
            parent = Employee.objects.get(id=parent_id)
        except ObjectDoesNotExist:
            raise NotFound({'detail': 'parent is not found'})
        parent.add_child(**request.data)
        serializer = EmployeeSerializer(Employee.objects.get(**request.data))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
