from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from employees.models import Employee
from employees.serializers.employee_serializer import EmployeeOutputSerializer, EmployeeInputSerializer
from rest_framework import filters

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.get_tree()
    serializer_class = EmployeeOutputSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'position', 'employment_date', 'salary']
    ordering_fields = ['id', 'first_name', 'last_name', 'position', 'employment_date', 'salary']

    # func for using different serializers for input and output
    def get_serializer_class(self):
        if self.action == 'create':
            return EmployeeInputSerializer
        return EmployeeOutputSerializer

    def create(self, request, *args, **kwargs):
        # get chief for creating employee
        chief_id = request.data.pop('chief_id')
        try:
            chief = Employee.objects.get(id=chief_id)
        except ObjectDoesNotExist:
            raise NotFound({'detail': 'chief is not found'})

        # create employee by adding employee as child(subordinate) to chief
        chief.add_child(**request.data)

        serializer = EmployeeOutputSerializer(Employee.objects.get(**request.data))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
