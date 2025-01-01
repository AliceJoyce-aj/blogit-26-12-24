from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username=models.CharField(max_length=100)
    useremail=models.CharField(max_length=100)
    userphone=models.CharField(max_length=100)
    userpassword=models.CharField(max_length=100)