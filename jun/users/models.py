from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    other_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.PositiveIntegerField()
    birthday = models.PositiveIntegerField()
    is_admin = models.CharField(max_length=64)


