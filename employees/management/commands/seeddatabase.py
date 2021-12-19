from django.core.management.base import BaseCommand, CommandError
from employees.models import Employee
from faker import Faker
from random import randint

class Command(BaseCommand):

    def create_boss(self):
        fake = Faker()
        boss = Employee.objects.create(
            path='000A',
            depth=1,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            position=fake.job(),
            employment_date=fake.date_time_between(start_date='-10y', end_date='now'),
            salary=randint(300000, 500000)
        )
        return boss

    def create_employees(self, boss, depth=1):
        fake = Faker()
        from collections import deque
        s = []
        s.append(boss)
        level = 1
        while s:
            print(s, level)
            n = len(s)
            level += 1
            for _ in range(n):
                p = s.pop()
                # for _ in range(2):
                data = {
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "position": fake.job(),
                    "employment_date": fake.date_time_between(start_date='-10y', end_date='now'),
                    "salary": randint(300000, 500000)
                }
                p.add_child(
                    first_name=data['first_name'],
                    last_name=data["last_name"],
                    position=data['position'],
                    employment_date=data['employment_date'],
                    salary=data['salary']
                )
                if level <= 5:
                    employee = Employee.objects.get(**data)
                    s.append(employee)
                    # for _ in range(2):
                    data = {
                        "first_name": fake.first_name(),
                        "last_name": fake.last_name(),
                        "position": fake.job(),
                        "employment_date": fake.date_time_between(start_date='-10y', end_date='now'),
                        "salary": randint(300000, 500000)
                    }
                    employee.add_sibling(**data)
                    child = Employee.objects.get(**data)
                    s.append(child)
                # if level <= 5:
                #     employee = Employee.objects.get(**data)
                #     s.append(employee)


    def handle(self, *ars, **options):
        print('Clearing DB')
        Employee.objects.all().delete()

        print(f'Start seeding database!')
        boss = self.create_boss()
        self.create_employees(boss)
