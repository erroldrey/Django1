from django.db import models
from datetime import date


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    other_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.PositiveIntegerField()
    birthday = date()
    is_admin = models.CharField(max_length=64)


class Project(models.Model):
    name = models.CharField(max_length=32, unique=True)
    users = models.ManyToManyField(User)
    repository = models.URLField(blank=True)

    def __str__(self):
        return self.name
