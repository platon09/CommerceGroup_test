from rest_framework import serializers
from employees.models import Employee


class EmployeeOutputSerializer(serializers.ModelSerializer):
    subordinate = serializers.SerializerMethodField(
        read_only=True, method_name="get_subordinate_nodes"
    )
    chief = serializers.SerializerMethodField(
        method_name="get_chief"
    )

    class Meta:
        model = Employee
        fields = ('id', 'depth', 'first_name', 'last_name', 'position',
                  'employment_date', 'salary', 'chief', 'subordinate')

    @staticmethod
    def get_subordinate_nodes(obj):
        subordinate_queryset = obj.get_children()
        return SubordinateSerializer(subordinate_queryset, many=True).data

    @staticmethod
    def get_chief(obj):
        chief = obj.get_parent()
        if chief is None:
            return "no chief"
        return ChiefSerializer(chief).data


class ChiefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position')


class SubordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'position', 'employment_date', 'salary')


class EmployeeInputSerializer(serializers.ModelSerializer):
    chief_id = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position', 'employment_date', 'salary', 'chief_id')
