from django.contrib.auth.models import User
from django.db import models

class Enterprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=255)
