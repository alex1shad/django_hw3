import json
from pathlib import Path
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = Path(__file__).resolve().parents[3] / 'fixtures' / 'books.json'
        with open(path, 'r', encoding='utf8') as file:
            books = json.load(file)
        for book in books:
            try:
                Book.objects.create(
                    id=book['pk'],
                    name=book['fields']['name'],
                    author=book['fields']['author'],
                    pub_date=book['fields']['pub_date']
                    )
            except:
                continue