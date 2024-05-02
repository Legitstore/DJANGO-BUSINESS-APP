from django.db import models

# Create your models here.
class AddUserModel(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    businessname = models.CharField(max_length=100, null=True)
    businessaddress = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)