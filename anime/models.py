from django.db import models
from django.db.models import *


class Anime(Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(blank=True, null=True)
    rating = IntegerField()
    studio = ForeignKey('Studio', related_name='animes', on_delete=CASCADE, default=1)

    def __str__(self):
        return self.title


class Studio(Model):
    name = CharField(max_length=100)
    base_city = CharField(max_length=50)

    def __str__(self):
        return self.name