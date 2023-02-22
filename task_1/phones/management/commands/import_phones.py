import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        path = Path(__file__).resolve().parents[3] / 'phones.csv'
        with open(path, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            Phone.objects.create(
                id=int(phone['id']),
                name=phone['name'],
                price=int(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists']
                )
