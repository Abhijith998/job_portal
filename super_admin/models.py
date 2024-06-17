from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class save_data(models.Model):
    checker_data=models.CharField(max_length=100)
    maker_data=models.CharField(max_length=100)

def __str__(self):
    return f"{self.checker_data} -> {self.maker_data}"