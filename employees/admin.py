from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(TreeAdmin):
    form = movenodeform_factory(Employee)
