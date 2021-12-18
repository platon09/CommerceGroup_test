from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from employees.models import Employee
from employees.serializers.employee_serializer import EmployeeSerializer, EmployeeTreeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from rest_framework import status
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.get_tree()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'first_name', 'last_name', 'position', 'employment_date', 'salary']
    ordering_fields = ['id', 'first_name', 'last_name', 'position', 'employment_date', 'salary']

    def create(self, request, *args, **kwargs):
        parent_data = request.data.pop('parent')
        parent = Employee.objects.get(**parent_data)
        parent.add_child(**request.data)
        serializer = self.get_serializer(Employee.objects.get(**request.data))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EmployeeTreeView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.get_tree()
    serializer_class = EmployeeTreeSerializer

    def list(self, request, *args, **kwargs):
        queryset = Employee.objects.filter(depth=1)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)