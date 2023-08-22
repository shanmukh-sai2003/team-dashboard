from django.db import models

# Create your models here.

class TeamMembers(models.Model):
    name = models.CharField(max_length = 32)
    role = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
