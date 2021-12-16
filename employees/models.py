from django.db import models
from djmoney.models.fields import MoneyField

from treebeard.mp_tree import MP_Node

class Employee(MP_Node):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    employment_date = models.DateTimeField(null=True, blank=True)
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT')

    node_order_by = ['first_name']

    def __str__(self):
        return 'Employee: {}'.format(self.first_name)
