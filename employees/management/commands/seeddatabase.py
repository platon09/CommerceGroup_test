from django.core.management.base import BaseCommand
from employees.models import Employee
from faker import Faker
from random import randint

fake = Faker()


def create_fake_data():
    data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "position": fake.job(),
        "employment_date": fake.date_time_between(start_date='-10y', end_date='now'),
        "salary": randint(300000, 500000)
    }
    return data


def create_boss():
    data = create_fake_data()
    data['path'] = '000A'
    data['depth'] = 1
    boss = Employee.objects.create(**data)
    return boss


def create_employees(boss):
    s = []
    s.append(boss)
    level = 1
    while s:
        n = len(s)
        level += 1
        for _ in range(n):
            p = s.pop()
            data = create_fake_data()
            p.add_child(**data)
            if level <= 5:
                employee = Employee.objects.get(**data)
                s.append(employee)
                for _ in range(5):
                    data = create_fake_data()
                    employee.add_sibling(**data)
                    child = Employee.objects.get(**data)
                    s.append(child)


class Command(BaseCommand):

    def handle(self, *ars, **options):
        print('Clearing DB')
        Employee.objects.all().delete()

        print(f'Start seeding database!')
        boss = create_boss()
        create_employees(boss)
