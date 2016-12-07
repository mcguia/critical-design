import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0, null=True)
    points = models.IntegerField(default=0, null=True)
    comments = models.IntegerField(default=0, null=False)


