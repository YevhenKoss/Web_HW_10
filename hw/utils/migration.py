import os

import django
from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw.settings')
django.setup()

from app_quotes.models import Quote, Author, Tag # noqa


client = MongoClient('mongodb://localhost')

db = client.hw10

authors = db.author.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quote.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(tag=tag)
        tags.append(t)
    exists_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))
    if not exists_quote:
        author = db.author.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)
