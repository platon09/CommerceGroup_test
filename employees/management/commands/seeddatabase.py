from django.core.management.base import BaseCommand, CommandError
from employees.models import Employee
from faker import Faker
from random import randint

class Command(BaseCommand):

    def create_boss(self):
        fake = Faker()
        boss = Employee.objects.create(
            depth=1,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            position=fake.job(),
            employment_date=fake.date_time_between(start_date='-10y', end_date='now'),
            salary=str(randint(300000, 500000))
        )

    def create_employees(self, bosses, depth):
        fake = Faker()
        depth += 1
        for boss in bosses:
            for _ in range(5):
                boss.add_child(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    position=fake.job(),
                    employment_date=fake.date_time_between(start_date='-10y', end_date='now'),
                    salary=str(randint(300000, 500000))
                )


    def handle(self, *ars, **options):
        print('Clearing DB')
        Employee.objects.all().delete()

        print(f'Start seeding database!')
        boss = self.create_boss()
        self.create_employees([boss], depth=1)
