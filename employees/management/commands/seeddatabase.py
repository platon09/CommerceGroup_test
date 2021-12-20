from django.core.management.base import BaseCommand
from employees.models import Employee
from faker import Faker
from random import randint

fake = Faker()

# generate fake data for employee
def create_fake_data():
    data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "position": fake.job(),
        "employment_date": fake.date_time_between(start_date='-10y', end_date='now'),
        "salary": randint(300000, 500000)
    }
    return data


# create the most important boss(first boss)
def create_boss():
    data = create_fake_data()
    data['path'] = '000A'
    data['depth'] = 1
    boss = Employee.objects.create(**data)
    return boss


def create_employees(boss):
    queue = []
    queue.append(boss)
    level = 1
    while queue:
        n = len(queue)
        level += 1
        for _ in range(n):
            chief = queue.pop()
            data = create_fake_data()
            chief.add_child(**data)
            if level <= 10:
                subordinate = Employee.objects.get(**data)
                queue.append(subordinate)
                for _ in range(50):
                    data = create_fake_data()
                    subordinate.add_sibling(**data)
                    colleague = Employee.objects.get(**data)
                    queue.append(colleague)


class Command(BaseCommand):

    def handle(self, *ars, **options):
        print('Clearing DB')
        Employee.objects.all().delete()

        print(f'Start seeding database!')
        boss = create_boss()
        create_employees(boss)
