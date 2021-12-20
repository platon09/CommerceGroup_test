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
        fields = ('id', 'depth', 'first_name', 'last_name', 'position',
                  'employment_date', 'salary', 'parent', 'children')

    @staticmethod
    def get_children_nodes(obj):
        child_queryset = obj.get_children()
        return ChildEmployeeSerializer(child_queryset, many=True).data

    @staticmethod
    def get_parent(obj):
        parent = obj.get_parent()
        if parent is None:
            return "no boss"
        return ParentSerializer(parent).data


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position')


class ChildEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position', 'employment_date', 'salary')


class CreateEmployeeSerializer(serializers.ModelSerializer):
    parent_id = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position', 'employment_date', 'salary', 'parent_id')
