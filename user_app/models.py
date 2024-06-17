from django.db import models
from django.contrib.auth.models import User
from admin_app.models import it_fields





class job_selection(models.Model):
    department=models.ForeignKey(it_fields,on_delete=models.CASCADE)
    state=models.CharField(max_length=100)
    job_type=models.CharField(max_length=100)
    username=models.CharField(max_length=100,blank=True,null=True)
    cv=models.FileField(upload_to='uploads/cvs/',blank=True,null=True)
   