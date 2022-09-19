import email
from django.db import models


# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True,primary_key=True)
    password=models.CharField(max_length=20)
    def __str__(self):
        return str(self.email)

class contacts(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    def __str__(self):
        return str(self.user_id)




