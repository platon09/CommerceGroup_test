from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(
        read_only=True, method_name="get_children_nodes"
    )
    parent = serializers.SerializerMethodField(
        method_name="get_parent"
    )

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position', 'employment_date', 'salary', 'parent', 'children')

    def get_children_nodes(self, obj):
        child_queryset = obj.get_children()
        return ChildEmployeeSerializer(child_queryset, many=True).data

    def get_parent(self, obj):
        parent = obj.get_parent()
        if parent is None:
            return "Босс"
        return ParentSerializer(parent).data


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position', 'employment_date', 'salary')

class ChildEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position', 'employment_date', 'salary')