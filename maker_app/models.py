
from django.contrib.auth.models import User

from django.db import models


class UserDetail(models.Model):
    username = models.CharField(max_length=100)
    cv = models.TextField()
    is_approved = models.BooleanField(default=False)

