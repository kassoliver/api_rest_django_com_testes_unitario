from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    user = models.ManyToManyField(User,related_name='companies')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
