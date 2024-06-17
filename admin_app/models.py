from django.db import models

# Create your models here.
class it_fields(models.Model):
    departments=models.CharField(max_length=100)

class related(models.Model):
    dept=models.ForeignKey(it_fields,on_delete=models.CASCADE)