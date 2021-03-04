from django.db import models

class User_Info(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField()