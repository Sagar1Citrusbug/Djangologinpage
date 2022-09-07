
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    cPassword = models.CharField(max_length=20)
    old_password = models.CharField(max_length=20)
    new_password = models.CharField(max_length=20)
    reenter_password = models.CharField(max_length=20)


    def __str__(self):
        return self.name



